import sys
from typing import List

from confluent_kafka import Consumer, KafkaError, KafkaException

from kafka_utils import ClientFactory


def start_consumer(consumer: Consumer, topics: List[str]):
    try:
        consumer.subscribe(topics)

        while True:
            msg = consumer.poll(timeout=1.0)
            if msg is None:
                continue
            if msg.error():
                if msg.error().code() == KafkaError._PARTITION_EOF:
                    # End of partition event
                    sys.stderr.write('%% %s [%d] reached end at offset %d\n' %
                                     (msg.topic(), msg.partition(), msg.offset()))
                    continue
                raise KafkaException(msg.error())

            print("Message received:")
            print(msg.value().decode('utf-8'))
    finally:
        # Close down consumer to commit final offsets.
        print("Closing consumer")
        consumer.close()


def main():
    args = ClientFactory.get_args(sys.argv[0])
    consumer = ClientFactory.get_consumer(host=args.kafka)
    start_consumer(consumer, ['discovery'])


if __name__ == "__main__":
    main()
