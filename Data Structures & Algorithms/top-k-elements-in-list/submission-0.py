class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash_map = {}
        for num in nums:
            if num not in hash_map:
                hash_map[num] = 0
            hash_map[num]+=1
        sorted_map =dict(sorted(hash_map.items(),key=lambda x:x[1])) 
        return list(sorted_map.keys())[-k:]

        