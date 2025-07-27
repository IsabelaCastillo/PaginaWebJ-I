# main.py
from fastapi import FastAPI
from rest_endpoint.endpoints import router

app = FastAPI()

# Montamos los endpoints bajo la ruta /saludo
app.include_router(router)

# Endpoint raíz opcional
@app.get("/")
def root():
    return {"mensaje": "API de prueba operativa"}
