from fastapi import APIRouter

from model.person import Person
import fake.person as service
from utils.tags import Tags

router = APIRouter(prefix="/person", tags=["person"])


@router.get("/")
def get_all() -> list[Person]:
    return service.get_all()


@router.get("/{name}")
def get_one(name: str) -> Person:
    return service.get_one(name)


@router.post("/")
def create(person: Person) -> Person:
    return service.create(person)


@router.put("/")
def replace(person: Person) -> Person:
    return service.create(person)


@router.patch("/")
def modify(person: Person) -> Person:
    return service.create(person)


@router.delete("/")
def delete(person: Person) -> Person:
    return service.create(person)
