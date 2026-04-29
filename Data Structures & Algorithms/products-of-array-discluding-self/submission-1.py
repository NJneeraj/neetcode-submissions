class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l = len(nums)
        res = [1]*l
        prefix = 1
        for i in range(l):
            res[i]=prefix
            prefix= prefix* nums[i]
        suffix = 1
        for i in range(l-1,-1,-1):
            res[i]*=suffix
            suffix*=nums[i]
        return res