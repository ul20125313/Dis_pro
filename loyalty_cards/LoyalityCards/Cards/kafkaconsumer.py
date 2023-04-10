from django.conf import settings
from kafka import KafkaConsumer
import json
from .models import Card

consumer = KafkaConsumer(
    settings.KAFKA_TOPIC_CARD_GENERATED,
    bootstrap_servers=settings.KAFKA_BOOTSTRAP_SERVERS,
    value_deserializer=lambda m: json.loads(m.decode('utf-8'))
)


def process_card_generated_message(message):
    card_id = message['id']
    card = Card.objects.get(pk=card_id)
    # Process the card here, e.g., save it to the database or update existing data.
    pass

def consume_messages():
    for message in consumer:
        print(f"Received message: {message.value}")
        process_card_generated_message(message.value)
