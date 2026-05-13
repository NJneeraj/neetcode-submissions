from collections import deque


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output = []
        d = deque()
        l = r = 0
        while r < len(nums):
            while d and nums[d[-1]] < nums[r]:
                d.pop()
            d.append(r)

            if l > d[0]:
                d.popleft()
            if (r + 1) >= k:
                l += 1
                output.append(nums[d[0]])
            r += 1

        return output
