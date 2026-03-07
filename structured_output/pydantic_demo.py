from pydantic import BaseModel , EmailStr , Field
from typing import Optional

class Student(BaseModel):
    name: str
    age: Optional[int] = None
    email: EmailStr
    cgpa: float = Field(gt=0  , lt=10 , description="Description" , default=5)


new_student= {'name': 'Deepak' , 'age': '32' , 'email': 'deepak@example.com'}

student = Student(**new_student)

# pydantic to dict
student_dict= dict(student)


#pydantic to json
student_json= student.model_dump_json()

print(student_json) 