import random

# Esta función genera soluciones vecinas
def generar_vecindario(s, todas_las_companias):
    vecindario = []
    for i in range(len(s)):
        for compania in todas_las_companias:
            if compania not in s:
                vecino = s[:]
                vecino[i] = compania
                vecindario.append(vecino)
    return vecindario

# Esta función evalúa una solución contando el número total de tecnologías únicas que puede cubrir
def evaluar_solucion(s):
    tecnologias = set()
    for compania in s:
        for tecnologia in compania:
            tecnologias.add(tecnologia)
    return len(tecnologias)

def tabu_search(C, k, max_iter):
    solucion_actual = random.sample(C, k)
    mejor_solucion = solucion_actual
    lista_tabu = []

    for _ in range(max_iter):
        vecindario = generar_vecindario(solucion_actual, C)

        # Descartamos soluciones que están en la lista tabú
        vecindario = [s for s in vecindario if s not in lista_tabu]

        # Evaluamos soluciones restantes
        vecindario_eval = [(s, evaluar_solucion(s)) for s in vecindario]

        # Elegimos mejor solución
        vecindario_eval.sort(key=lambda x: x[1], reverse=True)
        mejor_vecina, valor_mejor_vecina = vecindario_eval[0]
        solucion_actual = mejor_vecina
        if valor_mejor_vecina > evaluar_solucion(mejor_solucion):
            mejor_solucion = mejor_vecina

        # Actualizamos
        lista_tabu.append(mejor_vecina)
        if len(lista_tabu) > k:
            lista_tabu.pop(0)  # Eliminamos la solución más antigua

    return mejor_solucion
