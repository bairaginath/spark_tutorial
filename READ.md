Installation Hadoop Singlenode on Ubuntu 18.4
==============================================
https://dzone.com/articles/install-a-hadoop-cluster-on-ubuntu-18041

download HDP
--------------
wget http://apache.claz.org/hadoop/common/hadoop-3.1.1/hadoop-3.1.1.tar.gz
tar -xzvf hadoop-3.1.1.tar.gz
mv hadoop-3.1.1 /usr/local/hadoop

set JAVA_HOME and hadoop path on /etc/environment
-------------------------------------------------
PATH="/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/usr/local/hadoop/bin:/usr/local/hadoop/sbin"
JAVA_HOME="/usr/lib/jvm/java-8-openjdk-amd64/"

add a hadoop user and give them the correct permissions.
--------------------------------------------------------
adduser hadoop
usermod -aG hadoop hadoop
chown hadoop:root -R /usr/local/hadoop
chmod g+rwx -R /usr/local/hadoop

generate SSH key and copy this key
----------------------------------
su - hadoop
ssh-keygen -t rsa
ssh-copy-id hadoop@ubuntu

Configuring the Hadoop Master
-------------------------------
Open the /usr/local/hadoop/etc/hadoop/core-site.xml file and enter the following:

<configuration>
  <property>
    <name>fs.default.name</name>
    <value>hdfs://0.0.0.0:9000</value>
  </property>
</configuration>

Next, open the /usr/local/hadoop/etc/hadoop/hdfs-site.xml file and add the following:

<configuration>
  <property>
    <name>dfs.namenode.name.dir</name>
    <value>/usr/local/hadoop/data/nameNode</value>
  </property>
  <property>
    <name>dfs.datanode.data.dir</name>
    <value>/usr/local/hadoop/data/dataNode</value>
  </property>
  <property>
    <name>dfs.replication</name>
    <value>1</value>
  </property>
</configuration>

Format the HDFS file system
===========================
source /etc/environmnet
hdfs namenode -format

Now you can start HDFS
=======================
su - hadoop
hadoop@ubuntu:~$ start-dfs.sh

HDFS Web UI
===========
http://<ip-address>:9870




After Restart VM ,run as following
==================================
bairagi@ubuntu:~$ su hadoop
Password:
hadoop@ubuntu:/home/bairagi$ cd
hadoop@ubuntu:~$ start-dfs.sh
Starting namenodes on [0.0.0.0]
Starting datanodes
Starting secondary namenodes [ubuntu]
hadoop@ubuntu:~$



Download Spark Engine and Run
==============================
wget http://apache.claz.org/spark/spark-2.4.3/spark-2.4.3-bin-hadoop2.7.tgz
tar xvfz spark-2.4.3-bin-hadoop2.7.tgz
export SPARK_HOME="/home/bairagi/spark/spark-2.4.3-bin-hadoop2.7/"
$SPARK_HOME/bin/spark-submit spark_hdfs_write.py


Starting Yarn
=============
add ~/.bashrc file as below
export HADOOP_HOME="/usr/local/hadoop"
export HADOOP_COMMON_HOME=$HADOOP_HOME
export HADOOP_CONF_DIR=$HADOOP_HOME/etc/hadoop
export HADOOP_HDFS_HOME=$HADOOP_HOME
export HADOOP_MAPRED_HOME=$HADOOP_HOME
export HADOOP_YARN_HOME=$HADOOP_HOME

add configuration on  /usr/local/hadoop/etc/hadoop/yarn-site.xml file

  <property>
    <name>yarn.resourcemanager.hostname</name>
    <value>0.0.0.0</value>
  </property>

Run below command to start yarn
-------------------------------
hadoop@ubuntu:~$ start-yarn.sh
Starting resourcemanager
Starting nodemanagers
hadoop@ubuntu:~$

to list nodes
--------------
yarn node -list

to run spark application with yarn as below
--------------------------------------------
$SPARK_HOME/bin/spark-submit --master yarn --deploy-mode cluster  spark_yarn_hdfs_write.py

after that checking application list as below
---------------------------------------------
yarn app -list

to check application logs as below
-----------------------------------
yarn logs -applicationId <application_id>




Hadoop Web UI
--------------
http://<ip-address>:8088/cluster

