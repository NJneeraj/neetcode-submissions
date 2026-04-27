class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_map = {}
        for string in strs:
            count = [0]*26
            for char in string:
                count[ord(char)-ord("a")] +=1
            key = tuple(count)
            if key not in hash_map:
                hash_map[key] = []
            hash_map[key].append(string)
        return list(hash_map.values())
        