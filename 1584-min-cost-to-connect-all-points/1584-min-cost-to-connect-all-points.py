import heapq

class Solution:
    def minCostConnectPoints(self, points: list[list[int]]) -> int:
        n = len(points)
        # Суммарная минимальная стоимость
        total_cost = 0
        # Множество для хранения индексов посещенных точек
        visited = set()
        # Min-heap: быстрое извлечение ребра с минимальным весом (стоимость, индекс_точки)
        # Начинаем с первой точки (индекс 0) со стоимостью 0
        min_heap = [(0, 0)]
        
        while len(visited) < n:
            cost, current_point = heapq.heappop(min_heap)
            
            # Если точка уже добавлена в минимальное остовное дерево, пропускаем ее
            if current_point in visited:
                continue
                
            # Добавляем стоимость текущего ребра и помечаем точку как посещенную
            total_cost += cost
            visited.add(current_point)
            
            # Вычисляем расстояние до всех остальных непосещенных точек
            for next_point in range(n):
                if next_point not in visited:
                    # Манхэттенское расстояние
                    dist = abs(points[current_point][0] - points[next_point][0]) + abs(points[current_point][1] - points[next_point][1])
                    # Добавляем потенциальное ребро в кучу
                    heapq.heappush(min_heap, (dist, next_point))
                    
        return total_cost