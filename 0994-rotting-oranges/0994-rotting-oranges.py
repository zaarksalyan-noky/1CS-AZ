from collections import deque

class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        queue = deque()
        fresh_count = 0
        
        # Подсчитываем свежие апельсины и собираем координаты гнилых
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r, c))
                elif grid[r][c] == 1:
                    fresh_count += 1
                    
        minutes_passed = 0
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        # Запускаем BFS, пока есть элементы в очереди и свежие апельсины
        while queue and fresh_count > 0:
            minutes_passed += 1
            # Обрабатываем все апельсины, которые сгнили на текущей минуте
            for _ in range(len(queue)):
                r, c = queue.popleft()
                
                # Проверяем соседей
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    # Если сосед находится в пределах сетки и он свежий
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                        grid[nr][nc] = 2  # Апельсин начинает гнить
                        fresh_count -= 1
                        queue.append((nr, nc))
                        
        # Если остались недосягаемые свежие апельсины, возвращаем -1
        return minutes_passed if fresh_count == 0 else -1