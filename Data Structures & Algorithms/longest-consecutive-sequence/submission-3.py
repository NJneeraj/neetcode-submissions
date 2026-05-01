class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)
        longest=0
        for num in nums:
            if num-1 not in seen:
                val = num
                curr = 0
                while val in seen:
                    curr+=1
                    val+=1
                longest = max(longest,curr)
        return longest