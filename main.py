from typing import Annotated

from fastapi import FastAPI
from materias import dict_horario
app = FastAPI()


@app.get('/')
def root():
    return dict_horario


@app.get('/{carrera}')
def carrera(carrera: str, id: int | None = None):

    if id:
        return dict_horario[carrera][id]

    return dict_horario[carrera]
