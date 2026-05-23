class Solution:
    def findMin(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if i > 0 and nums[i] < nums[i-1]:
                return nums[i]
        return nums[0]