from fastapi import FastAPI
import datetime
from datetime import timedelta
import uuid
from fastapi import FastAPI, Body, status
from fastapi.responses import JSONResponse, FileResponse
 
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

app = FastAPI()

people = [Person("Tom", 38), Person("Bob", 42), Person("Sam", 28)]

# today = datetime.today().date()
# yesterday = today - timedelta(hours=3)

@app.get("/")
async def root():
    return {"greeting": "Hello, World!", "message": "Welcome to FastAPI!"}

@app.get("/get")
async def get_time():
    return {"time": datetime.datetime.now() - timedelta(hours=3, minutes=0)}

@app.get ("/api/info")
async def info():
    return {people}

@app.post ("api/place")
async def place(data=Body()):
    person = Person(data["name"], data["age"])
    people.append(person)
    return person
