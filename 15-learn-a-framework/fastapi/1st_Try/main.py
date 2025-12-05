from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Hello Biraj! FastAPI is working 🎉"}

@app.get("/user/{name}")
def say_hello(name: str):
    return {"message": f"Hello {name}"}

