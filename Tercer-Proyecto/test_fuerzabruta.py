from fuerza_bruta import fuerza_bruta 

def test_fuerza_bruta():
    S = {'x1', 'x2', 'x3', 'x4'}
    C = [
        {'nombre': 'Empresa1', 'tecnologias': {'x1', 'x2'}},
        {'nombre': 'Empresa2', 'tecnologias': {'x3'}},
        {'nombre': 'Empresa3', 'tecnologias': {'x4'}},
        {'nombre': 'Empresa4', 'tecnologias': {'x1', 'x2', 'x3'}}, 
]

    
    # caso en el que existe una solución
    k = 2
    resultado = fuerza_bruta(S, C, k)
    assert resultado is not None, 'Error en la prueba 1: se esperaba una solución, pero no se encontró ninguna.'
    
    # caso en el que no existe una solución
    k = 1   
    resultado = fuerza_bruta(S, C, k)
    assert resultado is None, 'Error en la prueba 2: no se esperaba ninguna solución, pero se encontró una.'
    
    # caso en el que todas las empresas cubren todas las tecnologías
    k = 4
    resultado = fuerza_bruta(S, C, k)
    assert resultado is not None, 'Error en la prueba 3: se esperaba una solución, pero no se encontró ninguna.'
    
    print('Todas las pruebas pasaron.')

test_fuerza_bruta()
