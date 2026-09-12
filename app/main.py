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

@app.get('/students/{student_name}')
def get_student_by_id(student_name:str):
    student = students_collection.find_one({"name":student_name},{"_id":0})
    if not student:
        return {"status":404,"message":"student not found"}
    return student