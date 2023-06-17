from busqueda_tabu import tabu_search, evaluar_solucion
def test_tabu_search():
    # Asumimos que cada empresa en C es un conjunto de tecnologías.
    C = [
        {"angular", "dotnet", "docker"},
        {"python", "java", "c++"},
        {"javascript", "node.js", "react"},
        {"mysql", "mongoDB", "redis"},
        {"docker", "kubernetes", "ansible"},
        {"git", "svn", "mercurial"}
    ]
    
    k = 3
    max_iter = 50

    print("Realizando búsqueda tabú...")
    resultado = tabu_search(C, k, max_iter)
    
    print("Resultado:")
    for i, compania in enumerate(resultado, 1):
        print(f"Compañía {i}: {compania}")

    print("Total de tecnologías cubiertas:", evaluar_solucion(resultado))

test_tabu_search()
