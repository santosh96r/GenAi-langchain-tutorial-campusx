from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class Student(BaseModel):
    name : str
    age : Optional[int] = None
    email : EmailStr = "abc@gmail.com"
    cgpa : Optional[float] = Field(gt=0, lt= 5) 


new_student = {"name":"Santosh", 'cgpa': 4}
# new_student = {'name': 55}
s1 = Student(**new_student)
# s2 = Student()

print(s1)