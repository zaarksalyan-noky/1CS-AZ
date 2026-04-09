class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        if not grid:
            return 0
            
        rows = len(grid)
        cols = len(grid[0])
        islands_count = 0
        
        def dfs(r, c):
            # Прерываем обход при выходе за границы или при попадании на воду ('0')
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == '0':
                return
                
            # Помечаем сушу как посещенную, превращая ее в воду
            grid[r][c] = '0'
            
            # Запускаем обход соседних клеток
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)
            
        # Проходим по всем элементам сетки
        for r in range(rows):
            for c in range(cols):
                # Если находим непосещенную часть острова
                if grid[r][c] == '1':
                    islands_count += 1
                    dfs(r, c)
                    
        return islands_count