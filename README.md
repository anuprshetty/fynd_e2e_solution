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
