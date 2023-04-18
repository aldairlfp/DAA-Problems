import random

def generar_muro_aleatorio(n, min_altura, max_altura):
    return [random.randint(min_altura, max_altura) for _ in range(n)]

from busqueda_ternaria import busqueda_ternaria, costo_total as costo_total_ter
from Fuerza_Bruta import fuerza_bruta, costo_total as costo_total_fb

for _ in range(300):
    # Generar un muro aleatorio y costos aleatorios para agregar, quitar y mover bloques
    muro_aleatorio = generar_muro_aleatorio(7, 1, 50)
    c_aleatorio = random.randint(1, 10)
    d_aleatorio = random.randint(1, 10)
    m_aleatorio = random.randint(1, 10)

    altura_min = min(muro_aleatorio)
    altura_max = max(muro_aleatorio)

    # Calcular la altura óptima y la energía consumida utilizando búsqueda ternaria
    altura_optima_ter = busqueda_ternaria(muro_aleatorio, c_aleatorio, d_aleatorio, m_aleatorio, altura_min, altura_max)
    altura_optima_ter = round(altura_optima_ter)
    energia_ter = costo_total_ter(muro_aleatorio, altura_optima_ter, c_aleatorio, d_aleatorio, m_aleatorio)

    # Calcular la altura óptima y la energía consumida utilizando fuerza bruta
    altura_optima_fb, energia_fb = fuerza_bruta(muro_aleatorio, c_aleatorio, d_aleatorio, m_aleatorio)

    # Comprobar que las alturas óptimas y las energías consumidas sean iguales
    assert altura_optima_ter == altura_optima_fb, f"Alturas óptimas no coinciden: {altura_optima_ter} != {altura_optima_fb}"
    assert energia_ter == energia_fb, f"Energías consumidas no coinciden: {energia_ter} != {energia_fb}"

print("Los resultados de ambos métodos coinciden en todos los casos.")
