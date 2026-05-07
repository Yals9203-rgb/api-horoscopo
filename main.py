from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class DatosUsuario(BaseModel):
    nombre: str
    edad: int
    signo: str

@app.get("/")
def home():
    return {"status": "Online", "mensaje": "API de Horóscopo lista para usar"}

@app.post("/obtener_suerte")
def calcular_suerte(usuario: DatosUsuario):
    # Una lógica simple para que el programa "haga algo"
    suerte = (usuario.edad % 10) + len(usuario.signo)
    
    consejos = [
        "Hoy es un gran día para aprender algo nuevo.",
        "La paciencia será tu mejor aliada en el trabajo.",
        "Un encuentro inesperado te traerá una sonrisa.",
        "Confía en tu instinto para esa decisión difícil."
    ]
    
    # Seleccionamos un consejo basado en el cálculo
    resultado = consejos[suerte % len(consejos)]
    
    return {
        "prediccion": f"Hola {usuario.nombre}, para tu signo {usuario.signo}: {resultado}",
        "numero_suerte": suerte
    }