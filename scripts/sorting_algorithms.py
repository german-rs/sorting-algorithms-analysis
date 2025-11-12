"""
scripts/sorting_algorithms.py
Implementación simple de Bubble Sort y funciones auxiliares mínimas.
"""

from typing import List, Tuple

def bubble_sort(arr: List[int]) -> List[int]:
    """
    Implementación sencilla de bubble sort.
    Recibe una lista de enteros y devuelve una lista ordenada.
    Notas:
    - Es in-place en la versión clásica, pero aquí devolvemos una copia
    para evitar modificar la lista original durante experimentos.
    - Mantuvimos la versión más clara posible para fines didácticos
    """
    a = arr.copy()
    n = len(a)
    # Bucle exterior: cada pasada coloca el siguiente mayor al final
    for i in range(n):
        # Bucle interior: comparar elementos adyacentes
        for j in range(0, n-i-1):
            if a[j] > a[j+1]:
                # intercambiar
                a[j], a[j+1] = a[j+1], a[j]
    return a

def is_sorted(arr: List[int]) -> bool:
    """ Comprueba si la lista está ordenada ascendentemente."""
    return all(arr[i] <= arr[i+1] for i in range(len(arr)-1))

# Bloque para probar manualmente si corre el script directo
if __name__ == '__main__':
    ejemplo = [5, 2, 9, 1, 5, 6]
    print("Original:", ejemplo)
    ordenado = bubble_sort(ejemplo)
    print("Ordenado:", ordenado)
    print("Está ordenado?", is_sorted(ordenado))


