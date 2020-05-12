from collections import defaultdict
import heapq

class Grafo:

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
            
    def obter_grau(self, vertice):
        grau = len(self.get_adjacentes(vertice))
        return grau

    def obter_grau_entrada(self, vertice):
        count = 0
        for adj in self.grafo.values():
            if vertice in adj:
                count += 1
        return count

    def eh_regular(self):
        count = 0
        for vertice in self.grafo.keys():
            grauAtual = self.obter_grau(vertice)
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


    def eh_completo_v2(self):
        qtd_vertices = len(self.grafo.keys())
        for vertice in self.grafo:
            if (self.obter_grau(vertice) != (qtd_vertices - 1)):
                return False
        return True


    def eh_conexo(self):
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


    def dijkstra(self, inicial, final):
        menores_distancias = {}
        antecessores = {}
        vertices_nao_visitados = self.grafo.copy()
        infinito = float('inf')
        caminho = []

        for vertice in vertices_nao_visitados:
            menores_distancias[vertice] = infinito
        menores_distancias[inicial] = 0

        while vertices_nao_visitados:
            min_vertice = None
            for vertice in vertices_nao_visitados:
                if min_vertice is None:
                    min_vertice = vertice
                elif menores_distancias[vertice] < menores_distancias[min_vertice]:
                    min_vertice = vertice

            for vertice_adjacentes, peso in self.grafo[min_vertice].items():
                if peso + menores_distancias[min_vertice] < menores_distancias[vertice_adjacentes]:
                    menores_distancias[vertice_adjacentes] = peso + menores_distancias[min_vertice]
                    antecessores[vertice_adjacentes] = min_vertice
            vertices_nao_visitados.pop(min_vertice)

        vertice_atual = final
        while vertice_atual != inicial:
            try:
                caminho.insert(0, vertice_atual)
                vertice_atual = antecessores[vertice_atual]
            except KeyError:
                print('caminho inacessível')
                break
        caminho.insert(0,inicial)
        if menores_distancias[final] != infinito:
            print('A menor distancia é ' + str(menores_distancias[final]))
            print('E o caminho é ' + str(caminho))

    def prim(self, raiz):
        arvore_minima = defaultdict(set)
        visitados = set([raiz])
        arestas = [
            (peso, raiz, vizinho)
            for vizinho, peso in self.grafo[raiz].items()
        ]
        heapq.heapify(arestas)
        while arestas:
            peso, frm, vizinho = heapq.heappop(arestas)
            if vizinho not in visitados:
                visitados.add(vizinho)
                arvore_minima[frm].add(vizinho)
                for proximo, peso in self.grafo[vizinho].items():
                    if proximo not in visitados:
                        heapq.heappush(arestas, (peso, vizinho, proximo))
        return dict(arvore_minima)


    def remover_vertice(self, vertice):
        if vertice in self.grafo.keys():
            del self.grafo[vertice]

        for vertices_adj in self.grafo.values():
            if vertice in vertices_adj:
                del vertices_adj[vertice]


    def ordenacao_topologica(self):
        copia = self.grafo.copy()
        vertices_grau_zero = list()
        ordem_topologica = list()

        def ordenacao():
            for vertice in self.grafo.keys():
                if self.obter_grau_entrada(vertice) == 0:
                    vertices_grau_zero.append(vertice)

            while vertices_grau_zero:
                v = vertices_grau_zero.pop(0)
                ordem_topologica.append(v)
                self.remover_vertice(v)
            
            while self.grafo:
                ordenacao()

        if len(self.grafo) != 0:
            ordenacao()
        
        self.grafo = copia
        return ordem_topologica



    def __str__(self):
        return f' {self.grafo}'