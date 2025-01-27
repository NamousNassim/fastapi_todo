from fastapi import FastAPI
from api.routes import todo_router

app = FastAPI()
app.include_router(todo_router)

@app.get("/")
def index():
    return {"message": "hello world"}