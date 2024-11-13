import uvicorn
from fastapi import FastAPI, Path, Query

from web import country, person


# from web import routers


# from pydantic import Field

app = FastAPI()

# app.include_router(routers.router)

app.include_router(person.router)
app.include_router(country.router)


@app.get("/main", tags=["Main"])
async def get_items(item: str):
    return {"item": item}


@app.get("/main/{item_id}", tags=["Main"])
async def get_specific_item(item_id: int = Path(...), query: str = Query(...)):
    return {"item_id": item_id, "query": query}


if __name__ == "__main__":

    uvicorn.run("main:app", reload=True)
