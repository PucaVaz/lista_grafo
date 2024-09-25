from grafo_processador import GrafoProcessador
import os
import time

def main():
    processador = GrafoProcessador()
    pasta_instancias = "./instncias_grafo"

    no_origem = 4
    no_destino = 7

    if not os.path.exists(pasta_instancias):
        print(f"A pasta '{pasta_instancias}' não existe.")
        return

    for nome_arquivo in os.listdir(pasta_instancias):
        if nome_arquivo.endswith(".txt"):
            caminho_arquivo = os.path.join(pasta_instancias, nome_arquivo)
            try:
                print(f"\nProcessando {nome_arquivo} com Matriz de Adjacência:")

                processador.ler_grafo_de_arquivo(caminho_arquivo, tipo_grafo='matriz')

                inicio_bfs_matriz = time.time()
                caminho_bfs_matriz = processador.bfs(caminho_arquivo, no_origem, no_destino)
                fim_bfs_matriz = time.time()

                if caminho_bfs_matriz is not None:
                    print(f"Caminho BFS (Matriz) de {no_origem} a {no_destino}: {caminho_bfs_matriz}")  
                print(f"Tempo BFS (Matriz): {fim_bfs_matriz - inicio_bfs_matriz:.6f} segundos")

                inicio_dfs_matriz = time.time()
                caminho_dfs_matriz = processador.dfs(caminho_arquivo, no_origem, no_destino) 
                fim_dfs_matriz = time.time()

                if caminho_dfs_matriz is not None:
                    print(f"Caminho DFS (Matriz) de {no_origem} a {no_destino}: {caminho_dfs_matriz}")  
                print(f"Tempo DFS (Matriz): {fim_dfs_matriz - inicio_dfs_matriz:.6f} segundos")
                
                print(f"\nProcessando {nome_arquivo} com Lista de Adjacência:")
 
                processador.ler_grafo_de_arquivo(caminho_arquivo, tipo_grafo='lista')

                inicio_bfs_lista = time.time()
                caminho_bfs_lista = processador.bfs(caminho_arquivo, no_origem, no_destino)
                fim_bfs_lista = time.time()

                if caminho_bfs_lista is not None:
                    print(f"Caminho BFS (Lista) de {no_origem} a {no_destino}: {caminho_bfs_lista}")  
                print(f"Tempo BFS (Lista): {fim_bfs_lista - inicio_bfs_lista:.6f} segundos")

                inicio_dfs_lista = time.time()
                caminho_dfs_lista = processador.dfs(caminho_arquivo, no_origem, no_destino)  
                fim_dfs_lista = time.time()

                if caminho_dfs_lista is not None:
                    print(f"Caminho DFS (Lista) de {no_origem} a {no_destino}: {caminho_dfs_lista}")  
                print(f"Tempo DFS (Lista): {fim_dfs_lista - inicio_dfs_lista:.6f} segundos")

            except Exception as e:
                print(f"Erro ao processar {nome_arquivo}: {e}")

if __name__ == "__main__":
    main()
