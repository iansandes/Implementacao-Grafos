class Grafo(object):

    """ Implementação de um grafo com lista de ajacencias"""

    def __init__(self):
        self.grafo = {}

    def adicionar_vertice(self, vertice):
        if vertice not in self.grafo.keys():
            self.grafo[vertice] = {}
    
    def adicionar_aresta(self, origem, destino, peso):
        for vertice in self.grafo.keys():
            if vertice == origem:
                adjacencias = self.grafo[vertice]
                adjacencias[destino] = peso
    
    def get_adjacentes(self, vertice):
        if vertice in self.grafo:
            adjacencia = self.grafo[vertice].keys()
            return adjacencia
            
    def __str__(self):
        return f' {self.grafo}'