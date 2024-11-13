from fastapi import HTTPException
from model.person import Person


_person = [
    Person(
        name="Paul",
        age=56,
        description="Veteran",
    ),
    Person(
        name="Henry",
        age=15,
        description="Young",
    ),
]


def get_all() -> list[Person]:
    return _person


def get_one(name: str) -> Person:
    for i in _person:
        if i.name == name:
            return i
        else:
            raise HTTPException(
                status_code=404,
                detail="Not found"
            )
    return None


def create(person: Person):
    return person


def update(person: Person):
    return person


def delete(person: Person):
    return person
