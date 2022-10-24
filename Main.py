from pydantic import BaseModel
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


# Runs on 8000 by default
app = FastAPI()
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ToDo(BaseModel):
    title: str
    status: str


@app.get("/")
def get_todos():
    return [{"title": "Take the dog for a walk", "status": "Created"}, {"title": "Finish writing this tutorial", "status": "In Progress"}]