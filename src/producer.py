import json
import sys
import time

from confluent_kafka import Producer

from kafka_utils import ClientFactory


def start_producer(producer: Producer, topic: str):
    index = 0
    while True:
        time.sleep(15)
        data = {'tag ': topic, 'data': [n for n in range(16)], 'index': index}
        json_data = json.dumps(data).encode('utf-8')
        producer.produce(topic, key=f"message_id_{index}", value=json_data)
        index += 1
        print(f"Message sent {json_data}")


def main():
    args = ClientFactory.get_args(sys.argv[0])
    producer = ClientFactory.get_producer(host=args.kafka)
    start_producer(producer, args.topic)


if __name__ == "__main__":
    main()
