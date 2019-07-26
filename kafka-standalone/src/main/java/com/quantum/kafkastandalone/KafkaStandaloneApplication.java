package com.quantum.kafkastandalone;

import org.springframework.boot.SpringApplication;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.boot.CommandLineRunner;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.kafka.core.KafkaTemplate;
import org.springframework.beans.factory.annotation.Autowired;

@SpringBootApplication
public class KafkaStandaloneApplication implements CommandLineRunner  {

	public static void main(String[] args) { 
	SpringApplication app = new SpringApplication(KafkaStandaloneApplication.class);
	        app.run(args);
	}

   
    @Autowired
     private KafkaTemplate<String, User> userKafkaTemplate;
     
      @Value(value = "${message.topic.name}")
      private String topicName;

   @Override
       public void run(String... arg0) throws Exception {
                    
	            while(true) {
	               User user=new User();
		       user.setName("bairagiJava");
		       user.setAge(23);
		       user.setEmail("bairagi.java@gmail.com");
		       userKafkaTemplate.send(topicName,user);
		        System.out.println("================================Pushing User data on kafka topic=========================");
			Thread.sleep(10000);
		    }
			    }
}
