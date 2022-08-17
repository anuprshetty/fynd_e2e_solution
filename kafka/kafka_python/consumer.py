from kafka import KafkaConsumer


topic = "fynd-json-product-event"
consumer = KafkaConsumer(topic)
print("consuming ...")

for message in consumer:
    print(f"message: {message}")
