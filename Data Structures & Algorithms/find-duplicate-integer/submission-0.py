class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        fast,slow = 0,0
        while True:
            slow = nums[slow] #1,2
            fast = nums[nums[fast]] #2,2
            if slow == fast:
                break
        secondSlow = 0
        while secondSlow != slow:
            secondSlow = nums[secondSlow]
            slow = nums[slow]
        return secondSlow
