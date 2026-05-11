class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        for l in range(len(nums)-k+1):
            max_num, i = nums[l], 0
            while i < k and  l + i < len(nums):
                max_num = max(nums[l + i], max_num)
                i += 1
            res.append(max_num)
        return res
