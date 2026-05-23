import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low, high = 1, max(piles)
        while low <= high:
            mid = (low + high) // 2
            total_hours = 0
            for i in range(len(piles)):
                total_hours += math.ceil(piles[i] / mid)
            if total_hours > h:
                low = mid + 1
            else:
                high = mid - 1
        return low
