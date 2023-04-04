from random import randint
from colorama import Fore
from busqueda_ternaria import busqueda_ternaria
from fuerza_bruta import fuerza_bruta


def generador(n):
    muestras = []
    pesos = []

    for i in range(n):
        size = randint(2, 10)
        l = [randint(2, 30) for j in range(size)]
        muestras.append(l)
        pesos.append((randint(1, 10), randint(1, 10), randint(1, 10)))

    return muestras, pesos


muestras, pesos = generador(10000)

for i in range(len(muestras)):
    test = busqueda_ternaria(
        muestras[i], pesos[i][2], pesos[i][1], pesos[i][0], min(muestras[i]), max(muestras[i]))
    safe = fuerza_bruta(muestras[i], pesos[i][0], pesos[i][1], pesos[i][2])
    if test == safe[0]:
        print(Fore.GREEN, safe, "==", test)
    else:
        print(Fore.RED, safe, "==", test)
    print(Fore.WHITE, muestras[i])
    print(Fore.WHITE, pesos[i])
