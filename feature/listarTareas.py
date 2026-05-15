import random
from typing import Iterable, List, TypeVar

T = TypeVar("T")

def listar_tareas_aleatorias(tareas: Iterable[T], cantidad: int | None = None) -> List[T]:
    """
    Devuelve una lista de tareas en orden aleatorio.
    Si cantidad es None, devuelve todas las tareas barajadas.
    """
    tareas_list = list(tareas)
    if not tareas_list:
        return []

    if cantidad is None or cantidad >= len(tareas_list):
        random.shuffle(tareas_list)
        return tareas_list

    return random.sample(tareas_list, k=cantidad)