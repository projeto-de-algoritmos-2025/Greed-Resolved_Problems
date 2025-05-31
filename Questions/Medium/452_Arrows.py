class Solution:
    def findMinArrowShots(self, points):
        # Ordena os intervalos dos balões pelo ponto final
        # Estratégia greedy de Interval Scheduling
        points.sort(key=lambda x: x[1])
        
        arrows = 0  # Contador de flechas necessárias
        current_end = float('-inf')  # Ponto onde foi disparada a última flecha
        
        # Itera sobre cada balão ordenado
        for start, end in points:
            # Se o balão atual começa depois do alcance da última flecha
            if start > current_end:
                arrows += 1         # Dispara uma nova flecha
                current_end = end   # Atualiza o ponto de disparo para o fim do balão atual
        
        return arrows  # Retorna o número mínimo de flechas necessárias
