class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        curr = []

        def dfs(i, total):
            if i >= len(nums):
                return

            curr.append(nums[i])
            if total + nums[i] == target:
                res.append(curr.copy())
            if total + nums[i] < target:
                dfs(i, total + nums[i])
            curr.pop()
            dfs(i + 1, total)

        dfs(0, 0)
        return res
