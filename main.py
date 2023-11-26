from fastapi import FastAPI
import datetime
from datetime import timedelta

app = FastAPI()

# today = datetime.today().date()
# yesterday = today - timedelta(hours=3)

@app.get("/")
async def root():
    return {"greeting": "Hello, World!", "message": "Welcome to FastAPI!"}

@app.get("/get")
async def get_time():
    return {"time": datetime.datetime.now() - timedelta(hours=3, minutes=0)}
