from fastapi import FastAPI, Body, Path, Query
from fastapi.responses import HTMLResponse, JSONResponse
from typing import List
from movie_schema import Movie


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


@app.get('/movies', tags=['movies',], response_model=List[Movie], status_code=200)
def get_movies() -> List[Movie]:
    print(movies)
    return JSONResponse(status_code=200, content=movies)


@app.get('/movies/{id}', tags=['movies',], response_model=Movie, status_code=200)
def get_movie(id: int = Path(ge=1, le=2000)) -> Movie:
    for item in movies:
        if item["id"] == id:
            return JSONResponse(status_code=200, content=item)
    return JSONResponse(status_code=404, content=[])


@app.get('/movies/', tags=['movies',], response_model=List[Movie], status_code=200)
def get_movies_by_category(category: str = Query(min_length=5, max_length=15), year: int = Query(le=2023)) -> List[Movie]:
    data = [item for item in movies if category in item['category'] and item['year'] == str(year)]
    return JSONResponse(status_code=200, content=data)


@app.post('/movies', tags=['movies',], response_model=Movie, status_code=201)
def create_movie(movie: Movie) -> Movie:
    movies.append(movie)
    return JSONResponse(status_code=201, content=dict(movies[-1]))


@app.put('/movies/{id}', tags=['movies',], response_model=dict, status_code=200)
def update_movie(id: int, movie: Movie) -> dict:
    for item in movies:
        if item["id"] == id:
            item['title'] = movie.title
            item['overview'] = movie.overview
            item['year'] = movie.year
            item['rating'] = movie.rating
            item['category'] = movie.category
            return JSONResponse(status_code=200, content={"message": "La pelicula se ha actualizado!"})
    return JSONResponse(status_code=404, content=[])


@app.delete('/movies/{id}', tags=['movies',], response_model=dict, status_code=200)
def delete_movie(id: int) -> dict:
    for item in movies:
        if item["id"] == id:
            movies.remove(item)
            return JSONResponse(status_code=200, content={"message": "La pelicula se ha eliminado!"})
    return JSONResponse(status_code=404, content={"message": "La pelicula con el id " + str(id) + " no existe!"})


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
