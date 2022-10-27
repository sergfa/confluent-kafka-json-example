# Using Kafka with confluent_kafka library

An example how to use confluent_kafka python library to produce and consume json messages

## docker-compose.yml

* Replace localhost with hostname of your machine or leave it as is if you run it on your local machine
* Copy docker-compose.yml to your machine

## Run docker compose

`docker-compose -f docker-compose.yml up -d`

## Connect to Kafka shell

`docker exec -it kafka /bin/sh`

## Create discovery Kafka topic

All Kafka shell scripts are located in /opt/kafka_<version>/bin:

`kafka-topics.sh --create --zookeeper zookeeper:2181 --replication-factor 1 --partitions 1 --topic discovery`

Verify that topic was created:

`kafka-topics.sh --list --zookeeper zookeeper:2181`

## Install python dependencies


`pip install requirements.txt`

## Update IP/HOST 

Update HOST variable in kafka_utils.py with ip address of Kafka machine


## Run producer

`python producer.py localhost`

## Run consumer

`python consumer.py localhost`