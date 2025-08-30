from pydantic import BaseModel, EmailStr, Field
from typing import Optional, Annotated

# class Student(BaseModel):
#     name : str
#     age : Optional[int] = None
#     email : EmailStr = "abc@gmail.com"
#     cgpa : Optional[float] = Field(gt=0, lt= 5) 


# new_student = {"name":"Santosh", 'cgpa': 4}
# # new_student = {'name': 55}
# s1 = Student(**new_student)
# # s2 = Student()

# print(s1)

class Student(BaseModel):
    name : Annotated[str, "name of student"]
    age : int 


stu = {"name": "skr", "age" : 22}
s1 = Student(**stu)
print(s1.name)