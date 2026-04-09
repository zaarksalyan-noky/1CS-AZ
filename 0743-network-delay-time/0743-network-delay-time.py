import heapq
from collections import defaultdict

class Solution:
    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:
        # Строим направленный граф в виде списка смежности
        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))
            
        # Очередь с приоритетом хранит кортежи (текущее_затраченное_время, узел)
        pq = [(0, k)]
        
        # Словарь для фиксации минимального времени достижения каждого узла
        min_times = {}
        
        while pq:
            current_time, node = heapq.heappop(pq)
            
            # Если кратчайший путь до узла уже найден, пропускаем его
            if node in min_times:
                continue
                
            # Фиксируем время для текущего узла
            min_times[node] = current_time
            
            # Добавляем в очередь всех соседей текущего узла
            for neighbor, weight in graph[node]:
                if neighbor not in min_times:
                    heapq.heappush(pq, (current_time + weight, neighbor))
                    
        # Если сигнал достиг всех n узлов, возвращаем максимальное время
        if len(min_times) == n:
            return max(min_times.values())
            
        # Если в графе есть недостижимые узлы
        return -1