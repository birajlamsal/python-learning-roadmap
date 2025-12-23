from tokenize import endpats
from fastapi.params import Body
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Post(BaseModel):
    title: str
    content: str

    # brand: str
    # name:str
    # year:int

@app.get("/")
async def root():
    return {"Hello Dog"}

@app.get("/posts")
async def posts():
    return {"message": "Hello Posts"}

@app.get("/login")
async def login():
    return {"message": "Hello Login"}

@app.get("/logout")
async def logout():
    return {"message": "Hello Logout"}

@app.post("/create")
async def create_post(store: dict = Body(...)):
    print(store)
    return{
        "New_Post": f"Title: {store['title']}  Content: {store['content']}"
        }

@app.post("/createpost")
async def create_post(store: dict = Body(...)):
    print(store)
    return{
        "New_Bike": f"Brand: {store['brand']}  Name: {store['name']} Year: {store['year']}"
        }

@app.post("/applepost")
async def apple_post(cat_post: Post):
    print (cat_post)
    return{
        "data":"New Post"}