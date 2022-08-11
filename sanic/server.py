from sanic import Sanic
from sanic import response


app = Sanic("HelloWorldApp")


@app.get("/")
async def home(request):
	return response.text("Hello, World!")
