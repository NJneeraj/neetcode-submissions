class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        multiplications=[]
        for l in range(len(nums)):
            multiply=1
            for i in range(len(nums)):
                if i!=l:
                    multiply *= nums[i]
            multiplications.append(multiply)
        return multiplications