class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        my_dict={};
        for x in nums:
            if my_dict.get(x) is not None:
                return True
            else:
                my_dict.update({x:x})
        return False