# Función de búsqueda ternaria
def busqueda_ternaria(muro_actual, c, d, m, l, r, eps=1):
    # Se repite hasta que la diferencia entre r y l sea menor o igual que eps
    print(r, l)
    while r - l > eps:
        # Encuentra los dos puntos intermedios m1 y m2 en el rango de búsqueda
        m1 = l + (r - l) / 3
        m2 = r - (r - l) / 3
        print(m1, m2)

        # Calcula el costo total para las alturas m1 y m2
        costo_m1 = costo_total(muro_actual, m1, c, d, m)
        costo_m2 = costo_total(muro_actual, m2, c, d, m)

        # Si el costo total en m1 es menor que en m2, se actualiza el límite superior r
        if costo_m1 < costo_m2:
            r = m2
        # De lo contrario, se actualiza el límite inferior l
        else:
            l = m1
    # Devuelve la altura óptima aproximada
    return l

# Función para calcular el costo total de energía consumida para construir el muro en la altura h
def costo_total(muro_actual, h, c, d, m):
    bloques_sobrantes = 0
    bloques_faltantes = 0

    # Calcula la cantidad de bloques sobrantes y faltantes para alcanzar la altura h
    for columna in muro_actual:
        if columna > h:
            bloques_sobrantes += columna - h
        else:
            bloques_faltantes += h - columna

    # Calcula la energía consumida para mover bloques
    energia_mover = 0
    if m < c + d:
        bloques_mover = min(bloques_sobrantes, bloques_faltantes)
        energia_mover = bloques_mover * m
        bloques_sobrantes -= bloques_mover
        bloques_faltantes -= bloques_mover

    # Calcula la energía consumida para agregar y quitar bloques
    energia_agregar = bloques_faltantes * c
    energia_quitar = bloques_sobrantes * d

    # Devuelve el costo total de energía
    return energia_mover + energia_agregar + energia_quitar

# Ejemplo de uso
muro_actual = [3, 5, 2, 6, 4]
costo_agregar = 5
costo_quitar = 3
costo_mover = 6

altura_min = min(muro_actual)
altura_max = max(muro_actual)

# Encuentra la altura óptima utilizando búsqueda ternaria
altura_optima = busqueda_ternaria(
    muro_actual, costo_agregar, costo_quitar, costo_mover, altura_min, altura_max)
altura_optima = round(altura_optima)

# Calcula la energía consumida para construir el muro en la altura óptima
energia = costo_total(muro_actual, altura_optima,
                      costo_agregar, costo_quitar, costo_mover)
print(f"Altura óptima: {altura_optima}")
print(f"Energía consumida: {energia}")
