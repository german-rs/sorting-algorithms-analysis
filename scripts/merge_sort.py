def merge_sort(arr):
    """
    Algoritmo de ordenamiento Merge Sort (Ordenamiento por Mezcla).

    Este algoritmo implementa la estrategia divide y conquista, dividiendo
    recursivamente el arreglo en mitades hasta obtener subarreglos de un solo
    elemento. Posteriormente, mezcla estos subarreglos de forma ordenada mediante
    un proceso de fusión (merge) que compara y combina los elementos,
    reconstruyendo gradualmente el arreglo completo en orden ascendente.

    Complejidad temporal:
        - Mejor caso: O(n log n)
        - Caso promedio: O(n log n)
        - Peor caso: O(n log n)

    Complejidad espacial: O(n) - Requiere espacio adicional para subarreglos

    Estabilidad: Estable - preserva el orden relativo de elementos iguales

    Características adicionales:
        - Rendimiento predecible y consistente en todos los casos
        - No es un algoritmo in-place debido al uso de memoria auxiliar
        - Altamente paralelizable

    Parámetros:
        arr (list): Lista de elementos comparables a ordenar

    Retorna:
        list: Nueva lista con los elementos ordenados en orden ascendente
    """
    if len(arr) <= 1:
        return arr

    # Dividir el arreglo en dos mitades
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    # Mezclar las mitades ordenadas
    return merge(left, right)


def merge(left, right):
    """
    Función auxiliar que mezcla dos arreglos ordenados en uno solo ordenado.

    Parámetros:
        left (list): Primera lista ordenada
        right (list): Segunda lista ordenada

    Retorna:
        list: Lista resultante de la mezcla ordenada
    """
    result = []
    i = j = 0

    # Comparar elementos de ambas listas y agregar el menor
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Agregar elementos restantes de left
    result.extend(left[i:])

    # Agregar elementos restantes de right
    result.extend(right[j:])

    return result


# Ejemplo
numeros = [38, 27, 43, 3, 9, 82, 10]
print("Original:", numeros)
ordenado = merge_sort(numeros)
print("Ordenado:", ordenado)