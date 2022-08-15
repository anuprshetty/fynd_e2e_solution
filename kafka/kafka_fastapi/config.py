import asyncio


KAFKA_BOOTSTRAP_SERVERS = "localhost:9092"
KAFKA_TOPIC = "fynd-json-product-event"
KAFKA_CONSUMER_GROUP = "group-id"

event_loop = asyncio.get_event_loop()
