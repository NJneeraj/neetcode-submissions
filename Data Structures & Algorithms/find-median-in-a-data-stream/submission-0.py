import heapq


class MedianFinder:
    def __init__(self):
        self.left = []
        self.right = []

    def addNum(self, num: int) -> None:
        l, r = len(self.left), len(self.right)

        if not l:
            heapq.heappush(self.left, -num)
            return None
        lMax = -self.left[0]
        if lMax > num:
            heapq.heappush(self.left, -num)
        else:
            heapq.heappush(self.right, num)

        while len(self.right) > len(self.left):
            heapq.heappush(self.left, -heapq.heappop(self.right))
        while len(self.left) > len(self.right) + 1:
            heapq.heappush(self.right, -heapq.heappop(self.left))

    def findMedian(self) -> float:
        l = len(self.left)
        r = len(self.right)
        if l == r:
            return (-self.left[0] + self.right[0]) / 2
        else:
            return -self.left[0]
