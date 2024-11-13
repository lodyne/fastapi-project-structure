from fastapi import HTTPException
from model.country import Country


_countries = [
    Country(name="Lody", area="Dar", aka="Bongo", description="Busy city"),
    Country(name="Lui", area="Dom", aka="East Zoo", description="capital city"),
]


def get_all() -> list[Country]:
    return _countries


def get_one(name: str) -> Country | None:
    for _country in _countries:
        if _country.name == name:
            return _country
        else:
            raise HTTPException(
                status_code=404,
                detail="Not found"
            )
    return None


def create(country: Country) -> Country:
    return country


def update(country: Country) -> Country:
    return country


def delete(country: Country) -> Country:
    return country
