class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash_map = {}
        for num in nums:
            if num not in hash_map:
                hash_map[num] = 0
            hash_map[num]+=1
        counts =[[] for _ in range(len(nums)+1)] 

        for num,count in hash_map.items():
            counts[count].append(num)
        my_list=[]
        for i in range(len(counts)-1,0,-1):
            for num in counts[i]:
                my_list.append(num)
                if len(my_list)==k:
                    return my_list
        return my_list

        