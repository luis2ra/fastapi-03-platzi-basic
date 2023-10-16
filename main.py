from fastapi import FastAPI, Body
from fastapi.responses import HTMLResponse, JSONResponse


app = FastAPI()
app.title = "Mi app con FastAPI"
app.version = "1.0.0"

movies = [ 
    {
        "id": 1,
        "title": "Avatar",
        "overview": "Un mundo de fantasia en Pandora",
        "year": "2009",
        "rating": 7.8,
        "category": "Accion/Ciencia Ficcion"
    },
    {
        "id": 2,
        "title": "Avatar 2",
        "overview": "Un mundo de fantasia en Pandora",
        "year": "2022",
        "rating": 8.8,
        "category": "Accion/Ciencia Ficcion"
    }
]

@app.get('/', tags=['home',])
def message():
    return HTMLResponse("<h2>Hola Mundo</h2>")


@app.get('/movies', tags=['movies',])
def get_movies():
    return JSONResponse(movies)


@app.get('/movies/{id}', tags=['movies',])
def get_movie(id: int):
    for item in movies:
        if item["id"] == id:
            return item
    return []


@app.get('/movies/', tags=['movies',])
def get_movies_by_category(category: str, year: int):
    return [item for item in movies if category in item['category'] and item['year'] == str(year)]


@app.post('/movies', tags=['movies',])
def create_movie(id: int = Body(), title: str = Body(), overview: str = Body(), year: int = Body(), rating: float = Body(), category: str = Body()):
    movies.append({
        "id": id,
        "title": title,
        "overview": overview,
        "year": year,
        "rating": rating,
        "category": category
    })
    return movies[-1]


@app.put('/movies/{id}', tags=['movies',])
def update_movie(id: int, title: str = Body(), overview: str = Body(), year: int = Body(), rating: float = Body(), category: str = Body()):
    for item in movies:
        if item["id"] == id:
            item['title'] = title
            item['overview'] = overview
            item['year'] = year
            item['rating'] = rating
            item['category'] = category
            return movies
    return []


@app.delete('/movies/{id}', tags=['movies',])
def delete_movie(id: int):
    for item in movies:
        if item["id"] == id:
            movies.remove(item)
            return movies
    return {"message": "La pelicula con el id " + str(id) + " no existe!"}


'''
Notes:

$ uvicorn main:app
$ uvicorn main:app --reload
$ uvicorn main:app --reload --port 8080
$ uvicorn main:app --reload --port 8080 --host 0.0.0.0

# en el navegador puede verse la documentacion autogenerada
http://127.0.0.1:8080/docs

http://127.0.0.1:8080/redoc

'''
