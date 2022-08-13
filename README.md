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
