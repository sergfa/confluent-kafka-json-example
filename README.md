# Using Kafka with confluent_kafka library

An example how to use confluent_kafka python library to produce and consume json messages
You can use an existing kafka broker or to run a docker kafka container
The docker-compose.yaml is provided 

## docker-compose.yml

* Replace localhost with hostname of your machine or leave it as is if you are planning to run docker container on your local machine
* Copy docker-compose.yml to your machine

## Run docker compose

`docker-compose -f docker-compose.yml up -d`

## Connect to Kafka shell

`docker exec -it kafka /bin/sh`

## Create Kafka topic

All Kafka shell scripts are located in /opt/kafka_<version>/bin:

`kafka-topics.sh --create --zookeeper zookeeper:2181 --replication-factor 1 --partitions 1 --topic my_first_topic`

Verify that topic was created:

`kafka-topics.sh --list --zookeeper zookeeper:2181`

## Install python dependencies


`pip install requirements.txt`

## Run producer

`python producer.py localhost --topic my_first_topic`

## Run consumer

`python consumer.py localhost --topic my_first_topic`