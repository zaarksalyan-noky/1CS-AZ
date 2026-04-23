from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
            
        # rob1: макс прибыль до дома i-2
        # rob2: тоже самое до дома i-1
        rob1 = 0 
        rob2 = 0 
        
        for n in nums:
            # Выбираем максимальную выгоду: 
            # грабить текущий дом + rob1 ИЛИ оставить выгоду от прошлого (rob2)
            temp = max(n + rob1, rob2)
            rob1 = rob2
            rob2 = temp
            
        return rob2       