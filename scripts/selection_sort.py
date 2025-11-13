def selection_sort(arr):
    """
    Algoritmo de ordenamiento Selection Sort (Ordenamiento por Selección).

    Este algoritmo divide conceptualmente el arreglo en dos regiones: una región
    ordenada y una región desordenada. En cada iteración, selecciona el elemento
    mínimo de la región desordenada y lo intercambia con el primer elemento de
    dicha región, expandiendo progresivamente la región ordenada hasta completar
    el ordenamiento total del arreglo.

    Complejidad temporal:
        - Mejor caso: O(n²)
        - Caso promedio: O(n²)
        - Peor caso: O(n²)

    Complejidad espacial: O(1) - Algoritmo in-place

    Estabilidad: Inestable

    Parámetros:
        arr (list): Lista de elementos comparables a ordenar

    Retorna:
        list: La misma lista ordenada en orden ascendente
    """
    n = len(arr)

    for i in range(n - 1):
        # Buscar el índice del elemento mínimo
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j

        # Intercambiar
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

    return arr


# Ejemplo
numeros = [64, 25, 12, 22, 11]
print("Original:", numeros)
selection_sort(numeros)
print("Ordenado:", numeros)