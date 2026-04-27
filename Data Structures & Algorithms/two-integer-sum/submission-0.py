class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_map = {}
        for i in range(len(nums)):
            x = nums[i]
            sub = num_map.get(target-x)
            if sub is None:
                num_map[x]=i
            else:
                return [sub,i]
        return None