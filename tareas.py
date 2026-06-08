"""
Parte III - API Serverless para Vercel (api/tareas.py)
Actividad 3.2 - Laboratorio IV

NOTA IMPORTANTE: En serverless el estado (lista 'tareas') NO persiste entre
invocaciones. Cada peticion puede ejecutarse en una instancia distinta.
Para una demo de laboratorio funciona; para produccion se usaria una base
de datos (ej. Vercel KV, Postgres, etc.). Esto es justamente parte de la
reflexion sobre escalabilidad.
"""
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI(title="API Serverless - Laboratorio IV")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


class Tarea(BaseModel):
    id: Optional[int] = None
    titulo: str
    descripcion: str
    completada: bool = False


tareas: List[Tarea] = []


@app.get("/api/tareas")
async def listar_tareas():
    return tareas


@app.post("/api/tareas")
async def crear_tarea(tarea: Tarea):
    tarea.id = len(tareas) + 1
    tareas.append(tarea)
    return {"mensaje": "Tarea creada exitosamente", "tarea": tarea}


@app.delete("/api/tareas/{tarea_id}")
async def eliminar_tarea(tarea_id: int):
    for i, t in enumerate(tareas):
        if t.id == tarea_id:
            del tareas[i]
            return {"mensaje": "Tarea eliminada exitosamente"}
    raise HTTPException(status_code=404, detail="Tarea no encontrada")
