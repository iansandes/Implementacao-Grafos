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
        vertices = []
        if vertice in self.grafo:
            adjacencia = self.grafo[vertice].keys()
            for vertice in adjacencia:
                vertices.append(vertice)
            return vertices

    def ehRegular(self):
        count = 0
        for vertice in self.grafo.keys():
            grauAtual = len(self.get_adjacentes(vertice))
            if(count > 0 and (grauAtual != grauAntigo)):
                return False
            grauAntigo = grauAtual
            count += 1
        return True

    def eh_completo(self):
        
        qtd_arestas = 0
        qtd_vertices = len(self.grafo)
        for aresta in self.grafo.values():
            qtd_arestas += len(aresta)


                   
        calculo_grafo_completo = (qtd_vertices * (qtd_vertices - 1))/2
        
        if (qtd_arestas/2) == calculo_grafo_completo:
            return True
        
        return False

    def grau(self, vertice):
        grau = 0
        for grau in range(len(self.get_adjacentes(vertice))):
            grau += 1
        return grau

    def ehConexo(self):
        conexo = 0
        def busca_profundidade(self, vertice):
            visitados.add(vertice)
            for vizinho in self.grafo[vertice]:
                if vizinho not in visitados:
                    busca_profundidade(self, vizinho)

        visitados = set()
        for vertice in self.grafo:
            if not vertice in visitados:
                busca_profundidade(self, vertice)
                conexo += 1
        if conexo == 1:
            return True
        else:
            return False



    def __str__(self):
        return f' {self.grafo}'