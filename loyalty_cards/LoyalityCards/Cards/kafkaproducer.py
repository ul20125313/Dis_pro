from django.conf import settings
from kafka import KafkaProducer
import json

producer = KafkaProducer(bootstrap_servers=settings.KAFKA_BOOTSTRAP_SERVERS,
                         value_serializer=lambda v: json.dumps(v).encode('utf-8'))

def send_message(topic, message):
    producer.send(topic, message)
    producer.flush()