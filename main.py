from fastapi import FastAPI


app = FastAPI()
app.title = "Mi app con FastAPI"
app.version = "1.0.0"

@app.get('/', tags=['home',])
def message():
    return { "gretting": "hola!" }


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
