class Solution:
    def floodFill(self, image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:
        start_color = image[sr][sc]
        
        # Если начальный цвет совпадает с новым, перекрашивание не требуется
        if start_color == color:
            return image
            
        rows = len(image)
        cols = len(image[0])
        
        def dfs(r, c):
            # Проверка выхода за границы матрицы и совпадения цвета пикселя
            if r < 0 or r >= rows or c < 0 or c >= cols or image[r][c] != start_color:
                return
                
            # Закрашиваем текущий пиксель новым цветом
            image[r][c] = color
            
            # Рекурсивно обходим соседние пиксели по вертикали и горизонтали
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)
            
        # Запускаем обход с заданных координат
        dfs(sr, sc)
        return image