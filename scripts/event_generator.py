import json, time, random
from kafka import KafkaProducer

# Connect to AWS MSK Kafka broker
MSK_BROKER = "<MSK_BROKER_ENDPOINT>"

producer = KafkaProducer(
    bootstrap_servers=MSK_BROKER,
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

events = ["page_view", "add_to_cart", "purchase"]

# Generate and stream events every second
while True:
    event = {
        "user_id": random.randint(1, 1000),
        "event": random.choice(events),
        "product_id": random.randint(1, 500),
        "amount": round(random.uniform(10.5, 500.75), 2),
        "timestamp": int(time.time())
    }
    producer.send("ecommerce-events", event)
    print("Sent:", event)
    time.sleep(1)
