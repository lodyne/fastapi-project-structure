from pydantic import BaseModel


class Country(BaseModel):
    name: str
    area: str
    aka: str
    description: str


# raw = {"name": "Lody", "area": "Dar", "aka": "Bongo", "description": "Kwa wajanja"}
# data = Country(**raw)
# print(data)
