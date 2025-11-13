def insertion_sort(arr):
    """
    Algoritmo de ordenamiento Insertion Sort (Ordenamiento por Inserción).

    Este algoritmo construye incrementalmente un arreglo ordenado tomando un
    elemento a la vez de la porción no ordenada e insertándolo en su posición
    correcta dentro de la porción ya ordenada. El proceso es análogo al método
    utilizado para ordenar cartas en la mano, donde cada nueva carta se inserta
    en su ubicación apropiada entre las cartas previamente ordenadas.

    Complejidad temporal:
        - Mejor caso: O(n) - cuando el arreglo está ordenado o casi ordenado
        - Caso promedio: O(n²)
        - Peor caso: O(n²) - cuando el arreglo está en orden inverso

    Complejidad espacial: O(1) - Algoritmo in-place

    Estabilidad: Estable - preserva el orden relativo de elementos iguales

    Características adicionales:
        - Algoritmo adaptativo: su rendimiento mejora con datos parcialmente ordenados
        - Eficiente para conjuntos de datos pequeños

    Parámetros:
        arr (list): Lista de elementos comparables a ordenar

    Retorna:
        list: La misma lista ordenada en orden ascendente
    """
    n = len(arr)

    for i in range(1, n):
        key = arr[i]
        j = i - 1

        # Mover elementos mayores que key una posición adelante
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        # Insertar key en su posición correcta
        arr[j + 1] = key

    return arr


# Ejemplo
numeros = [12, 11, 13, 5, 6]
print("Original:", numeros)
insertion_sort(numeros)
print("Ordenado:", numeros)
