from pydantic import BaseModel, Field


class Person(BaseModel):
    name: str = Field(...)
    age: int
    description: str
