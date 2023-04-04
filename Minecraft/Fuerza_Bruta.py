def costo_total(muro_actual, h, c, d, m):
    bloques_sobrantes = 0
    bloques_faltantes = 0

    # Calcular bloques sobrantes y faltantes en cada columna
    for columna in muro_actual:
        if columna > h:
            bloques_sobrantes += columna - h
        else:
            bloques_faltantes += h - columna

    # Calcular la energía consumida para mover bloques
    energia_mover = 0
    if m < c + d:
        bloques_mover = min(bloques_sobrantes, bloques_faltantes)
        energia_mover = bloques_mover * m
        bloques_sobrantes -= bloques_mover
        bloques_faltantes -= bloques_mover

    # Calcular la energía consumida para agregar y quitar bloques
    energia_agregar = bloques_faltantes * c
    energia_quitar = bloques_sobrantes * d

    # Devolver la energía total consumida
    return energia_mover + energia_agregar + energia_quitar

def fuerza_bruta(muro_actual, c, d, m):
    # Inicializar la altura mínima y máxima posible para el muro
    altura_min = min(muro_actual)
    altura_max = max(muro_actual)

    # Inicializar el costo mínimo y la altura óptima como "infinito" y "None" respectivamente
    costo_minimo = float("inf")
    altura_optima = None

    # Iterar desde la altura mínima hasta la altura máxima (ambas inclusive)
    for altura in range(altura_min, altura_max + 1):
        # Calcular el costo total para la altura actual utilizando la función costo_total
        costo = costo_total(muro_actual, altura, c, d, m)

        # Si el costo calculado es menor que el costo mínimo actual, actualizar el costo mínimo y la altura óptima
        if costo < costo_minimo:
            costo_minimo = costo
            altura_optima = altura

    # Devolver la altura óptima y el costo mínimo
    return altura_optima, costo_minimo
