# fynd_e2e_solution
Onboarding demo project

## FastAPI

- [documentation](https://fastapi.tiangolo.com)
- [source code](https://github.com/tiangolo/fastapi)
- FastAPI stands on the shoulders of giants:
    - [Starlette for the web parts](https://www.starlette.io/) - Starlette is a lightweight ASGI framework/toolkit, which is ideal for building async web services in Python.
    - [Pydantic for the data parts](https://pydantic-docs.helpmanual.io/) - pydantic enforces type hints at runtime, and provides user-friendly errors when data is invalid.
- uvicorn --> ASGI server (Asynchronous Server Gateway Interface)

- commands:
  - pip install fastapi
  - pip install "uvicorn[standard]"
  - uvicorn app:app --reload

## Sanic

- Next generation Python web server/framework | Build fast. Run fast.
- To provide a simple way to get up and running a highly performant HTTP server that is easy to build, to expand, and ultimately to scale.
- [documentation](https://sanic.dev/en/guide/)
- [source code](https://github.com/sanic-org/sanic)

- commands:
  - pip install sanic
  - sanic server.app --port <port_number>

## marshmallow

- A Python Object Serialization and Deserialization Library.
- marshmallow is an ORM/ODM/framework-agnostic library for converting complex datatypes, such as objects, to and from native Python datatypes.
- An ORM maps between an Object Model and a Relational Database. An ODM maps between an Object Model and a Document Database. MySQL is not an ORM, it's a Relational Database, more specifically, a SQL Database. MongoDB is not an ODM, it's a Document Database.
- xyz is 'Framework agnostic' simply means that xyz does not depend on any framework. It is a great and much required idea that focuses on building libraries/components which are not dependent on any specific framework for their implementation, rather to develop a generic stuff to cater everyone.
- [documentation](https://marshmallow.readthedocs.io/en/stable/)

- commands:
  - pip install marshmallow

## MongoDB

- [documentation](https://www.mongodb.com/docs/)
- [installation](https://www.mongodb.com/docs/manual/tutorial/install-mongodb-on-os-x/)
- [basics tutorial](https://www.youtube.com/watch?v=ofme2o29ngU)
- [mongodb aggregation framework](https://www.youtube.com/watch?v=A3jvoE0jGdE&list=PLWkguCWKqN9OwcbdYm4nUIXnA2IoXX0LI)
- [mongodb GUI](https://robomongo.org/)
- upsert --> The term upsert is a portmanteau – a combination of the words “update” and “insert.” In the context of relational databases, an upsert is a database operation that will update an existing row if a specified value already exists in a table, and insert a new row if the specified value doesn't already exist.

- commands:
  - mongosh
  - cls
  - exit
  - show dbs
  - db
  - use <db_name>
  - db.dropDatabase()
  - show collections
  - db.collection_name.insertOne({name: "Anup"})
  - db.collection_name.insertMany([{name: "Anup"}, {name: "Ravi", age: 25}])
  - db.collection_name.find()
  - db.collection_name.find().limit(2)
  - db.collection_name.find().sort({name: -1, age: 1}).limit(2)
  - db.collection_name.find().skip(1).limit(2)
  - db.collection_name.find({name: "Anup"})
  - db.collection_name.findOne({name: "Anup"})
  - db.collection_name.countDocuments({name: "Anup"})
  - db.collection_name.find({name: "Anup"}, {name: 1, age: 1, _id: 0})
  - db.collection_name.find({name: {$ne: "Anup"}})
  - db.collection_name.updateOne({_id: ObjectId("6303d1a6ee47664d92572f88")}, {$set: {age: 27}})
  - db.collection_name.updateMany({age: 26}, {$set: {age: 27}})
  - db.collection_name.replaceOne({age: 26}, {name: "Ravi"})
  - db.collection_name.deleteOne({age: 26})

## Apache Kafka

- [documentation](https://kafka.apache.org/documentation/)
- [configuring Kafka for access across networks](https://www.confluent.io/blog/kafka-client-cannot-connect-to-broker-on-aws-on-docker-etc/)
- [kafdrop - kafka web ui](https://github.com/obsidiandynamics/kafdrop)
- [kafka-shell](https://betterdatascience.com/master-the-kafka-shell-in-5-minutes-topics-producers-and-consumers-explained/)
- [kafka-python](https://timber.io/blog/hello-world-in-kafka-using-python/)
- [kafka-fastapi](https://www.youtube.com/watch?v=l5NOe3jTEso)
- [kafka-sanic](https://github.com/naruvimama/falcon)
- Apache Kafka is a distributed event store and stream-processing platform. A high-throughput distributed messaging system. Tool for building real time data pipelines. streaming/queueing/messaging system.
- It helps in decoupling of data streams and systems.
- Use cases:
  - Messaging System
  - Activity Tracking
  - Gather metrics from many locations
  - Application logs gathering
  - Stream processing (with Kafka streams API or Spark)
  - Decoupling of system dependencies
  - It provides connectors to import and export bulk data from databases and other systems.
  - Integration with Spark, Flink, Storm, Hadoop, and many more Big Data Technologies.
- Terminologies:
  - Producer --> An application that sends messages to Kafka.
  - Message --> Small to medium-sized piece of data. For Kafka, message is just an array of bytes.
  - Consumer --> An application that reads data from Kafka.
  - Broker --> Kafka Server
  - cluster --> A group of computers sharing workload for a common purpose. Kafka is a distributed system. So Kafka cluster has group of computers each executing one instance of Kafka broker.
  - Topic --> A topic is a unique name for Kafka stream. Kafka stores a stream of records in categories called topics. Each record consists of a key, value and a timestamp.
  - Partition:
    - Broker will store the data for a topic. This data can be huge. It may be larger than the storage capacity of a single computer. In this case, broker has a challenge in storing that data. 
    - One of the obvious solution is to break the data into two or more parts (partitions) and distribute them into multiple computers.
    - When we create a topic, we need to tell the number of partitions to create. And Kafka broker will create that many partitions for the topic. every partition sits on a single machine. You can not further break that partition again.
  - offset --> A sequence id given to messages as they arrive in a partition. These numbers once assigned, they never change. They are immutable. offset starts from 0. Offsets are local to the partition.
  - Global unique identifier of a message = Topic name + Partition number + Offset
  - consumer group --> A group of consumers acting as a single logical unit.
- References:
  - [integrating Apache Kafka With Python Asyncio Web Applications](https://www.confluent.io/blog/kafka-python-asyncio-integration/)
  - [confluent kafka in docker shell](https://developer.confluent.io/quickstart/kafka-docker/)
