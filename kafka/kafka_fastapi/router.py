import json

from fastapi import APIRouter
from schema import Message
import config
from aiokafka import AIOKafkaConsumer, AIOKafkaProducer


route = APIRouter()


@route.post('/create_message')
async def send(message: Message):
	producer = AIOKafkaProducer(loop=config.event_loop, bootstrap_servers=config.KAFKA_BOOTSTRAP_SERVERS)
	await producer.start()
	try:
		print(f"producer - sending the message with value: {message}")
		value_json = json.dumps(message.__dict__).encode('utf-8')
		await producer.send_and_wait(topic=config.KAFKA_TOPIC, value=value_json)
	finally:
		await producer.stop()


async def consume():
	consumer = AIOKafkaConsumer(config.KAFKA_TOPIC, loop=config.event_loop, bootstrap_servers=config.KAFKA_BOOTSTRAP_SERVERS, group_id=config.KAFKA_CONSUMER_GROUP)
	await consumer.start()
	try:
		async for message in consumer:
			print(f"consumer - message: {message}")
	finally:
		await consumer.stop()
