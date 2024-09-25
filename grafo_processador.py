from typing import List, Tuple, Optional

class GrafoProcessador:
    def __init__(self):
        self.grafos = {}

    class GrafoListaAdjacencia:
        def __init__(self, num_vertices: int):
            self.lista_adjacencia: List[List[Tuple[int, int]]] = [[] for _ in range(num_vertices)]

        def adicionar_aresta(self, v1: int, v2: int, peso: int = 1) -> None:
            self.lista_adjacencia[v1].append((v2, peso))
            self.lista_adjacencia[v2].append((v1, peso))

    class GrafoMatrizAdjacencia:
        def __init__(self, num_vertices: int):
            self.matriz_adjacencia: List[List[int]] = [[0] * num_vertices for _ in range(num_vertices)]

        def adicionar_aresta(self, v1: int, v2: int, peso: int = 1) -> None:
            self.matriz_adjacencia[v1][v2] = peso
            self.matriz_adjacencia[v2][v1] = peso

    def ler_grafo_de_arquivo(self, nome_arquivo: str, tipo_grafo: str = 'lista') -> None:
        with open(nome_arquivo, 'r') as arquivo:
            num_vertices = int(arquivo.readline().strip())
            
            if tipo_grafo == 'matriz':
                grafo = self.GrafoMatrizAdjacencia(num_vertices)
            elif tipo_grafo == 'lista':
                grafo = self.GrafoListaAdjacencia(num_vertices)
            else:
                raise ValueError("tipo_grafo deve ser 'lista' ou 'matriz'")
            
            for i in range(num_vertices):
                linha = list(map(int, arquivo.readline().strip().split()))
                for j in range(num_vertices):
                    peso = linha[j]
                    if peso != 0: 
                        grafo.adicionar_aresta(i, j, peso)
        
        self.grafos[nome_arquivo] = grafo

    def bfs(self, nome_grafo: str, s: int, t: int) -> Optional[List[int]]:
        grafo = self.grafos[nome_grafo]
        if isinstance(grafo, self.GrafoMatrizAdjacencia):
            return self._bfs_matriz(grafo, s, t)
        else:
            return self._bfs_lista(grafo, s, t)

    def _bfs_matriz(self, grafo: GrafoMatrizAdjacencia, s: int, t: int) -> Optional[List[int]]:
        num_vertices = len(grafo.matriz_adjacencia)
        visitado = [False] * num_vertices
        pai = [-1] * num_vertices
        fila = [s]
        visitado[s] = True

        while fila:
            vertice_atual = fila.pop(0)

            if vertice_atual == t:
                return self._reconstruir_caminho(pai, t)

            for vizinho in range(num_vertices):
                if grafo.matriz_adjacencia[vertice_atual][vizinho] != 0 and not visitado[vizinho]:
                    visitado[vizinho] = True
                    pai[vizinho] = vertice_atual
                    fila.append(vizinho)

        print("Não há caminho entre os vértices BFS Matriz")
        return None

    def _bfs_lista(self, grafo: GrafoListaAdjacencia, s: int, t: int) -> Optional[List[int]]:
        visitado = [False] * len(grafo.lista_adjacencia)
        pai = [-1] * len(grafo.lista_adjacencia)
        fila = [s]
        visitado[s] = True

        while fila:
            vertice_atual = fila.pop(0)

            if vertice_atual == t:
                return self._reconstruir_caminho(pai, t)

            for vizinho, _ in grafo.lista_adjacencia[vertice_atual]:
                if not visitado[vizinho]:
                    visitado[vizinho] = True
                    pai[vizinho] = vertice_atual
                    fila.append(vizinho)

        print("Não há caminho entre os vértices BFS Lista")
        return None

    def dfs(self, nome_grafo: str, s: int, t: int) -> Optional[List[int]]:
        grafo = self.grafos[nome_grafo]
        if isinstance(grafo, self.GrafoMatrizAdjacencia):
            return self._dfs_matriz(grafo, s, t)
        else:
            return self._dfs_lista(grafo, s, t)

    def _dfs_lista(self, grafo: GrafoListaAdjacencia, s: int, t: int) -> Optional[List[int]]:
        num_vertices = len(grafo.lista_adjacencia)
        visitado = [False] * num_vertices
        pai = [-1] * num_vertices
        pilha = [s]

        while pilha:
            vertice_atual = pilha.pop()

            if not visitado[vertice_atual]:
                visitado[vertice_atual] = True

                for vizinho, _ in grafo.lista_adjacencia[vertice_atual]:
                    if not visitado[vizinho]:
                        pilha.append(vizinho)
                        pai[vizinho] = vertice_atual 

        if not visitado[t]:
            print("Não há caminho entre os vértices DFS Lista")
            return None
        
        return self._reconstruir_caminho(pai, t)

    def _dfs_matriz(self, grafo: GrafoMatrizAdjacencia, s: int, t: int) -> Optional[List[int]]:
        num_vertices = len(grafo.matriz_adjacencia)
        visitado = [False] * num_vertices
        pai = [-1] * num_vertices
        pilha = [s]

        while pilha:
            vertice_atual = pilha.pop()

            if not visitado[vertice_atual]:
                visitado[vertice_atual] = True
                
                for vizinho in range(num_vertices):
                    if grafo.matriz_adjacencia[vertice_atual][vizinho] != 0 and not visitado[vizinho]:
                        pilha.append(vizinho)
                        pai[vizinho] = vertice_atual 
                        
        if not visitado[t]:
            print("Não há caminho entre os vértices DFS Matriz")
            return None
        
        return self._reconstruir_caminho(pai, t)

    def _reconstruir_caminho(self, pai: List[int], destino: int) -> List[int]:
        caminho = []
        while destino != -1:
            caminho.append(destino)
            destino = pai[destino]
        caminho.reverse()
        return caminho
