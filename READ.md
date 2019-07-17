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

