from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Bienvenue sur FastAPI!"}

@app.get("/second/")
def read_root():
    return {"message": "2eme page"}

