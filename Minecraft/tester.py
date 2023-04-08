from random import randint
from busqueda_ternaria import busqueda_ternaria
from fuerza_bruta import fuerza_bruta


def generador(n):
    muestras = []
    pesos = []

    for i in range(n):
        size = randint(2, 20)
        l = [randint(2, 30) for j in range(size)]
        muestras.append(l)
        pesos.append((randint(1, 10), randint(1, 10), randint(1, 10)))

    return muestras, pesos


muestras, pesos = generador(100)
for i in range(len(muestras)):
    bt = busqueda_ternaria(
        muestras[i], pesos[i][0], pesos[i][1], pesos[i][2], min(muestras[i]), max(muestras[i]))
    fb = fuerza_bruta(muestras[i], pesos[i][0], pesos[i][1], pesos[i][2])
    print('Fuerza bruta', fb[0], "<->", 'Busqueda ternaria', bt)
    print(muestras[i])
    print(pesos[i])
