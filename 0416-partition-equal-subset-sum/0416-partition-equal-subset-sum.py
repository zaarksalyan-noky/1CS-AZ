from typing import List

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total_sum = sum(nums)
        
        # Если общая сумма нечетная, деление без остатка невозможно
        if total_sum % 2 != 0:
            return False
            
        target = total_sum // 2
        # Множество для хранения всех достижимых сумм
        dp = set()
        dp.add(0)
        
        for num in nums:
            next_dp = set()
            for t in dp:
                # Если достигли нужной суммы, сразу возвращаем True
                if t + num == target:
                    return True
                
                # Добавляем в новое множество новую сумму и старую
                next_dp.add(t + num)
                next_dp.add(t)
            dp = next_dp
            
        return False