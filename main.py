from fastapi import FastAPI, Query, Body
import uvicorn

app = FastAPI()

hotel_db = [
    {'id': 1, 'title': 'Space', 'city': 'Moscow', },
    {'id': 2, 'title': 'BigBen', 'city': 'London', },
    {'id': 3, 'title': 'Tower', 'city': 'Paris', },
]


@app.get("/hotels")
def get_hotels():
    hotels = [hotel for hotel in hotel_db]

    return hotels


@app.delete("/hotels/{hotels_id}")
def delete_hotel(hotels_id: int):
    global hotel_db
    hotel_db = [hotel for hotel in hotel_db if hotels_id != hotel['id']]
    return {'status': 'ok'}



@app.put("/hotels/{hotel_id}", summary="Обновление отеля")
def put_hotel(hotel_id: int,
              title: str = Body(),
              city: str = Body()):
    global hotel_db
    for hotel in hotel_db:
        if hotel["id"] == hotel_id:
            hotel["title"] = title
            hotel["city"] = city
            break
    return {"status": "OK"}


@app.patch("/hotels/{hotel_id}", summary="Обновление части параметров отеля")
def patch_hotel(hotel_id: int,
                title: str | None = Body(),
                city: str | None = Body()):
    global hotel_db
    for hotel in hotel_db:
        if hotel["id"] == hotel_id:
            if title:
                hotel["title"] = title
            if city:
                hotel["city"] = city
            break
    return {"status": "OK"}


@app.post('/hotels')
def create_hotel(
        title: str = Body(embed=True, description="Название отеля"),
        city: str = Body(embed=True, description="Город отеля"),
):
    hotel_db.append(
        {'id': hotel_db[-1]['id'] + 1,
         'title': title,
         'city': city}
    )
    return {"status": "ok"}


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
