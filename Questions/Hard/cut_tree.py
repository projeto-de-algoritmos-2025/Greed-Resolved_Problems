import heapq
from typing import List

class Solution:
    def cutOffTree(self, forest: List[List[int]]) -> int:
        # Verifica se a posição inicial (0,0) é inacessível
        if forest[0][0] == 0:
            return -1

        m, n = len(forest), len(forest[0])  # Dimensões da matriz

        # Heurística usada pelo A*: distância de Manhattan
        def heuristic(x1, y1, x2, y2):
            return abs(x1 - x2) + abs(y1 - y2)

        # Algoritmo A* para encontrar o menor caminho entre start e goal
        def a_star(start, goal):
            sx, sy = start
            gx, gy = goal

            # heap: tuplas 
            heap = [(heuristic(sx, sy, gx, gy), 0, sx, sy)]
            visited = set()  # Conjunto de nós já expandidos

            while heap:
                f, g, x, y = heapq.heappop(heap)  # Nó com menor f
                if (x, y) == (gx, gy):
                    return g  # Chegou ao destino, retorna o custo real

                if (x, y) in visited:
                    continue
                visited.add((x, y))

                # Explora os vizinhos válidos 
                for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
                    nx, ny = x + dx, y + dy
                    # Verifica se a nova posição está dentro e é acessível
                    if 0 <= nx < m and 0 <= ny < n and forest[nx][ny] != 0 and (nx, ny) not in visited:
                        new_g = g + 1  # Custo acumulado até aqui
                        new_f = new_g + heuristic(nx, ny, gx, gy)  # Custo total estimado
                        heapq.heappush(heap, (new_f, new_g, nx, ny))  # Adiciona à fila
            return -1  

        # Lista de todas as árvores com altura > 1, ordenadas pela altura crescente
        trees = sorted(((i, j) for i in range(m) for j in range(n) if forest[i][j] > 1),
                       key=lambda x: forest[x[0]][x[1]])

        total_steps = 0
        curr = (0, 0) 

        # Para cada árvore, em ordem de altura, calcula a distância até ela com A*
        for tree in trees:
            steps = a_star(curr, tree)
            if steps == -1:
                return -1  # Alguma árvore é inacessível
            total_steps += steps  # Soma os passos necessários
            curr = tree  # Atualiza a posição atual para a árvore recém-cortada

        return total_steps  # Retorna o número total de passos
