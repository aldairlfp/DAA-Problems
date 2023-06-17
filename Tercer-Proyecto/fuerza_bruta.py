from itertools import combinations

def fuerza_bruta(S, C, k):
    # Generar todos los subconjuntos de tamaño k de C
    subconjuntos = combinations(C, k)
    
    # Para cada subconjunto
    for subconjunto in subconjuntos:
        # Unir todas las tecnologías requeridas por las empresas en el subconjunto
        tecnologias = set().union(*[empresa['tecnologias'] for empresa in subconjunto])
        
        # Comprobar si las tecnologías cubren exactamente todas las tecnologías en S
        if tecnologias == S:
            return subconjunto 
        
    return None


S = {'x1', 'x2', 'x3', 'x4'}
C = [
    {'nombre': 'Empresa1', 'tecnologias': {'x1', 'x2'}},
    {'nombre': 'Empresa2', 'tecnologias': {'x3'}},
    {'nombre': 'Empresa3', 'tecnologias': {'x4'}},
    {'nombre': 'Empresa4', 'tecnologias': {'x1', 'x2', 'x3', 'x4'}},
]

k = 2
resultado = fuerza_bruta(S, C, k)

if resultado:
    print('Se encontró una solución:')
    for empresa in resultado:
        print(empresa['nombre'])
else:
    print('No se encontró ninguna solución.')
