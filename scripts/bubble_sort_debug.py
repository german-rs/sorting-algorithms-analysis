def bubble_sort_debug(lista):
    """
    Bubble Sort con variables explícitas para facilitar el debugging.
    Coloca breakpoints en las líneas marcadas con # 🔴 BREAKPOINT
    """
    n = len(lista)  # 🔴 BREAKPOINT: Mira el tamaño de la lista
    print(f"=== Iniciando Bubble Sort ===")
    print(f"Lista original: {lista}")
    print(f"Cantidad de elementos: {n}\n")

    # Contador de pasadas completas
    pasada_numero = 0

    # Bucle externo: controla cuántas pasadas hacemos
    for i in range(n):
        pasada_numero += 1
        print(f"\n--- PASADA #{pasada_numero} ---")
        print(f"Estado actual de la lista: {lista}")

        # Flag para detectar si hubo intercambios
        hubo_intercambio = False

        # Bucle interno: comparaciones en esta pasada
        # (n - 1 - i) porque los últimos elementos ya están ordenados
        comparaciones_en_pasada = n - 1 - i
        print(f"Haremos {comparaciones_en_pasada} comparaciones en esta pasada")

        for j in range(n - 1 - i):  # 🔴 BREAKPOINT: Observa j cambiando
            # Elementos que vamos a comparar
            elemento_actual = lista[j]
            elemento_siguiente = lista[j + 1]

            print(f"\n  Comparación #{j + 1}:")
            print(f"  Posición {j}: {elemento_actual} vs Posición {j + 1}: {elemento_siguiente}")

            # 🔴 BREAKPOINT: Aquí es donde ocurre la comparación crítica
            if elemento_actual > elemento_siguiente:
                # Necesitamos intercambiar
                print(f"  ❌ {elemento_actual} > {elemento_siguiente} → INTERCAMBIAMOS")

                # Intercambio explícito (en lugar de usar tuplas)
                temporal = lista[j]
                lista[j] = lista[j + 1]
                lista[j + 1] = temporal

                hubo_intercambio = True
                print(f"  Estado después del intercambio: {lista}")
            else:
                # No intercambiamos
                print(f"  ✅ {elemento_actual} <= {elemento_siguiente} → NO intercambiamos")

        # Fin de la pasada
        print(f"\nFin de pasada #{pasada_numero}")
        print(f"Lista después de esta pasada: {lista}")

        # Optimización: si no hubo intercambios, ya está ordenada
        if not hubo_intercambio:
            print(f"\n🎉 ¡No hubo intercambios! La lista ya está ordenada.")
            break

    print(f"\n=== Bubble Sort Completado ===")
    print(f"Lista final ordenada: {lista}")
    print(f"Total de pasadas realizadas: {pasada_numero}")

    return lista


# ===== PROGRAMA PRINCIPAL =====
if __name__ == "__main__":
    # Lista de prueba pequeña para debugging
    mi_lista = [64, 34, 25, 12, 22, 11, 90]

    print("BUBBLE SORT - MODO DEBUG")
    print("=" * 50)

    # 🔴 BREAKPOINT: Coloca uno aquí y ejecuta paso a paso (F8)
    resultado = bubble_sort_debug(mi_lista)

    print(f"\n{'=' * 50}")
    print(f"RESULTADO FINAL: {resultado}")

    # Otras listas para probar:
    # mi_lista = [5, 2, 8, 1, 9]  # Lista pequeña
    # mi_lista = [1, 2, 3, 4, 5]  # Ya ordenada (mejor caso)
    # mi_lista = [5, 4, 3, 2, 1]  # Orden inverso (peor caso)