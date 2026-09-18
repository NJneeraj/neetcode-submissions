import heapq


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for [i,j] in points:
            sqr = i**2 + j**2
            heapq.heappush(heap,(-sqr,(i,j)))
            if len(heap) > k:
                heapq.heappop(heap)
        res =[]
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        return res
