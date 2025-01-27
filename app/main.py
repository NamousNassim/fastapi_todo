from fastapi import FastAPI
from api.routes import todo_routes

app = FastAPI()
app.include_router(todo_routes)

@app.get("/")
def index():
    return {"messsage":"hello world"}