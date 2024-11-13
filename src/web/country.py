from model.country import Country
from fastapi import APIRouter
# import fake.country as service
import service.country as service
from utils.tags import Tags

router = APIRouter(prefix="api/country", tags=["country"])


@router.get("/")
def get_all() -> list[Country]:
    return service.get_all()


@router.get("/{name}")
def get_one(name: str) -> Country:
    return service.get_one(name)


@router.post("/")
def create(country: Country) -> Country:
    return service.create(country)


@router.put("/")
def replace(country: Country) -> Country:
    return service.create(country)


@router.patch("/")
def modify(country: Country) -> Country:
    return service.create(country)


@router.delete("/")
def delete(country: Country) -> Country:
    return service.create(country)
