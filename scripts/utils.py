"""
scripts/utils.py
Funciones auxiliares mínimas: generación de datos y cronómetro simple.
"""

import random
import time
from typing import List, Callable, Tuple

def generar_lista(tamano: int, tipo: str = "aleatorio", semilla: int = 42) -> List[int]:
    """
    Genera una lista de enteros.
    :param tamano: Cantidad de elementos.
    :param tipo: 'aleatorio', 'ordenado', 'inverso'
    :param semilla: para reproducibilidad
    """
    random.seed(semilla)
    if tipo == "aleatorio":
        return [random.randint(0, tamano * 10) for _ in range(tamano)]
    if tipo == "ordenado":
        return list(range(tamano))
    if tipo == "inverso":
        return list(range(tamano, 0, -1))
    raise ValueError("Tipo debe ser aleatorio, ordenado, inverso.")


def medir_tiempo(func: Callable, *args, n_repeticiones: int= 3, **kwargs) -> Tuple[float, list]:
    """
    Mide el tiempo de ejecución de 'func(*args, **kwargs)' y devuelve:
    - tiempo_promedio (segundos)
    - lista_de_tiempos (segundos) de cada repetición
    Usa time.perf_counter() para mediciones de alta resolución
    """
    tiempos = []
    for _ in range(n_repeticiones):
        t0 = time.perf_counter()
        func(*args, **kwargs)
        t1 = time.perf_counter()
        tiempos.append(t1 - t0)
    promedio = sum(tiempos) / len(tiempos)
    return promedio, tiempos













