import sqlite3

from model.country import Country

DB_NAME = "country.db"
conn = sqlite3.connect(DB_NAME)
curs = conn.cursor()


def init():
    curs.execute("create table country(name,area,aka,description)")


def row_to_model(row: tuple) -> Country:
    name, area, aka, description = row
    return Country(name, area, aka, description)


def model_dict(country: Country) -> dict:
    return country.model_dump()


def get_one(name: str) -> Country:
    query = "select * from country where name=:name"
    params = {"name": name}
    curs.execute(query, params)
    row = curs.fetchone()
    return row_to_model(row)


def get_all(name: str) -> list[Country]:
    query = "select * from country"
    curs.execute(query)
    rows = list(curs.fetchall())
    return [row_to_model(row) for row in rows]


def create(country: Country):
    query = """insert into country values (:name,:description,:country,:area,:aka)"""
    params = model_dict(country)
    curs.execute(query, params)
    
def modify(country:Country):
    return country

def replace(country:Country):
    return country

def delete(country:Country):
    query="delete from country where name=:name"
    params={"name":country.name}
    curs.execute(query,params)