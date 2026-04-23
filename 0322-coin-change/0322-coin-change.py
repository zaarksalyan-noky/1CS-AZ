from typing import List

class Solution:
    def coinChange(self, coins: List[int], quant: int) -> int:
        # Инициализируем массив значением "бесконечность" (quant + 1)
        dp = [quant + 1] * (quant + 1)
        # Для суммы 0 нужно 0 монет
        dp[0] = 0
        
        # Проходим по всем суммам от 1 до quant
        for a in range(1, quant + 1):
            for c in coins:
                # Если монета помещается в текущую сумму
                if a - c >= 0:
                    # Обновляем минимальное количество монет
                    dp[a] = min(dp[a], 1 + dp[a - c])
                    
        # Если значение не изменилось, сумму собрать нельзя
        if dp[quant] != quant + 1:
            return dp[quant]
        else:
            return -1