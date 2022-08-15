from kafka import KafkaProducer
import json


bootstrap_servers = 'localhost:9092'
producer = KafkaProducer(bootstrap_servers=bootstrap_servers)

topic = 'fynd-json-product-event'
product_info = {
	"type": "Shoe",
	"brand": "Puma"
}

print("producing ...")
for i in range(3):
	slug = f"shoe-{i}"
	product_info["slug"] = slug
	message = {
		"key": f"product-shoe-{i}",
		"value": json.dumps(product_info)
	}
	producer.send(topic=topic, key=message["key"].encode(), value=message["value"].encode())
	print(f'{i}) topic: {topic}, key: {message["key"].encode()}, value: {message["value"].encode()}')
