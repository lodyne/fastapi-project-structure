from model.country import Country
import fake.country as data


def get_all() -> list[Country]:
    return data.get_all()


def get_one(name: str) -> Country:
    return data.get_one(name)


def create(country: Country) -> Country:
    return data.create(country)


def replace(country: Country) -> Country:
    return data.replace(country)


def modify(country: Country) -> Country:
    return data.modify(country)


def delete(country: Country) -> bool:
    return data.delete(country)
