from Grafo import Grafo


grafo = Grafo()

grafo.adicionar_vertice('a')
grafo.adicionar_vertice('b')
grafo.adicionar_vertice('c')
#grafo.adicionar_vertice('d')
g
rafo.adicionar_aresta('b', 'c', 5)
grafo.adicionar_aresta('c', 'b', 5)
grafo.adicionar_aresta('a', 'b', 3)
grafo.adicionar_aresta('b', 'a', 3)
grafo.adicionar_aresta('a', 'c', 4)
grafo.adicionar_aresta('c', 'a', 4)
#grafo.adicionar_aresta('a', 'd', 2)
#grafo.adicionar_aresta('d', 'a', 2)

print(grafo)
print(grafo.get_adjacentes('a'))
print(grafo.grau('a'))
print(grafo.ehRegular())
print(grafo.eh_completo())
print(grafo.ehConexo())