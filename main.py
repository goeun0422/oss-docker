from fastapi import FastAPI
from model import Course 
import json
import os

app = FastAPI()
FILE_NAME = "courses.json"

def ensure_file_exists():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, "w", encoding="utf-8") as f:
            json.dump([], f)

ensure_file_exists()

# (1) GET /courses: 전체 수강기록 반환
@app.get("/courses")
async def get_courses() -> list:
    with open(FILE_NAME, "r", encoding="utf-8") as f:
        data = json.load(f)
    return data

# (2) POST /courses: 새로운 수강기록 추가
@app.post("/courses")
async def add_course(course: Course) -> dict:
    with open(FILE_NAME, "r", encoding="utf-8") as f:
        data = json.load(f)
    
    data.append(course.dict())
    
    with open(FILE_NAME, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
        
    return {"msg": "Course added successfully"}