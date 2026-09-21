from collections import deque, Counter
import heapq


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = Counter(tasks)
        heap = [-count for task, count in freq.items()]
        heapq.heapify(heap)
        queue = deque([])
        i = 0
        while heap or queue:
            if len(queue) and queue[0][0] == i:
                _, frq = queue.popleft()
                heapq.heappush(heap, (-frq))
            if len(heap):
                frq = heapq.heappop(heap)
                remain = -frq - 1
                if remain > 0:
                    queue.append((i + n + 1, remain))
            i += 1
        return i
