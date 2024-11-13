from model.person import Person
from fake.person import data


def get_all() -> list[Person]:
    return data.get_all()


def get_one(name: str) -> Person:
    return data.get_one(name)


def create(person: Person) -> Person:
    return data.create(person)


def replace(person: Person) -> Person:
    return data.replace(person)


def modify(person: Person) -> Person:
    return data.modify(person)


def delete(person: Person) -> bool:
    return data.delete(person)
