class Solution:
    def climbStairs(self, n: int) -> int:
        # Базовые случаи для 1 и 2 ступенек
        if n <= 2:
            return n
        
        # prev1 хранит способы для шага n-1
        # prev2 хранит способы для шага n-2
        prev2 = 1
        prev1 = 2
        
        for i in range(3, n + 1):
            # Текущее количество способов равно сумме двух предыдущих
            current = prev1 + prev2
            prev2 = prev1
            prev1 = current
            
        return prev1