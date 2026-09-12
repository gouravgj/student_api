from fastapi import FastAPI
from app.database import students_collection

app = FastAPI()

@app.get('/')
def home():
    return {"status":200,"message":"success"}

@app.get("/students")
def get_students():
    students = list(students_collection.find({}, {"_id": 0}))
    return students