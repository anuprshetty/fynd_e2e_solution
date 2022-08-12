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
