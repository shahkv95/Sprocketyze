from typing import List
from pydantic import BaseModel, validator


class Employee(BaseModel):
    name: str
    age: int

    @validator("age")
    def age_validator(value):
        if value < 0:
            raise ValueError("Age cannot be less than 0")
        return value


employee = Employee(name="John Doe", age=35)
employee_data = employee.dict()
Employee.validate(employee_data)

employee2 = Employee(name="Minus 1", age=-1)
employee2_data = employee2.dict()
Employee.validate(employee2_data)
