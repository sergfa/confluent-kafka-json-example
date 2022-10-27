import argparse
import socket
from typing import Dict

from confluent_kafka import Consumer, Producer


class ClientFactory:
    HOST = 'localhost:9092'

    consumer_conf = {
        'bootstrap.servers': HOST,
        'group.id': "discovery_group",
        'auto.offset.reset': 'smallest'
    }
    producer_conf = {
        'bootstrap.servers': HOST,
        'client.id': socket.gethostname()
    }

    @staticmethod
    def get_config(source_config: Dict[str, str], host: str):
        conf = {**source_config}
        if host is not None:
            conf['bootstrap.servers'] = host
        return conf

    @staticmethod
    def get_consumer(host: str = None) -> Consumer:
        consumer = Consumer(ClientFactory.get_config(ClientFactory.consumer_conf, host))
        return consumer

    @staticmethod
    def get_producer(host: str = None):
        producer = Producer(ClientFactory.get_config(ClientFactory.producer_conf, host))
        return producer

    @staticmethod
    def get_args(prog_name: str):
        parser = argparse.ArgumentParser(prog=prog_name, description='Working with Kafka')
        parser.add_argument('kafka', help='Host/IP address of Kafka broker', type=str)
        args = parser.parse_args()
        return args
