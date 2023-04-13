from django.conf import settings
from kafka import KafkaProducer
import json
from kafka.errors import NoBrokersAvailable

from kafka.errors import KafkaError

try:
    producer = KafkaProducer(bootstrap_servers=settings.KAFKA_BOOTSTRAP_SERVERS,
                             value_serializer=lambda v: json.dumps(v).encode('utf-8'))
except NoBrokersAvailable:
    producer = None


def send_message(topic, message):
    if producer is not None:
        future = producer.send(topic, message)
        try:
            future.get(timeout=10)
        except KafkaError as e:
            print(f"Failed to send message: {e}")
    else:
        print("Kafka producer not available, message not sent.")