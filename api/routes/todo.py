from fastapi import APIRouter

todo_router = APIRouter(prefix='/api',tags=['Todo'])

@todo_router.get("/")
def all_todos():
    return "Soon"
@todo_router.post('/')
def post_todo():
    return 'nope'
@todo_router.put('/{key}')
def update_todo(key:int):
    return f'key = {key}'

@todo_router.delete('/{key}')
def delete_todo(key:int):
    return f'key = {key}'