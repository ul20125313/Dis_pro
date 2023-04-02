from kafka import KafkaConsumer
import json

consumer = KafkaConsumer(
    'your_topic',
    bootstrap_servers=['localhost:9092'],
    value_deserializer=lambda m: json.loads(m.decode('utf-8'))
)

def consume_messages():
    for message in consumer:
        print(f"Received message: {message.value}")
        process_message(message.value)

def process_message(message):
    # Process the message here, e.g., save it to the database or update existing data.
    pass
