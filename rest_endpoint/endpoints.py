# endpoints/saludo.py
from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def decir_hola():
    return {"mensaje": "Hola desde FastAPI"}

@router.get("/ventas/{dia}")
def saludar_persona(dia: int):
    return {"total": f" {dia+20}"}
