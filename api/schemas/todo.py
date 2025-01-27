from pydantic import BaseModel,Field 
from typing import Optional
from tortoise.contrib.pydantic import pydantic_model_creator
from api.models.todo import Todo
GetTodoSchema = pydantic_model_creator(Todo,name="Todo")
class PostTodo(BaseModel):
    task:str = Field(...,title="Task",description="Task to be done")
    done:bool 
class UpdateTodo(BaseModel):
    task:Optional[str] = Field(None,title="Task",description="Task to be done")
    done:Optional[bool] = Field(None,title="Done",description="Task status")
