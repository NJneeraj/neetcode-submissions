class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_map = {}
        for string in strs:
            key = "".join(sorted(string))
            if key not in hash_map:
                hash_map[key] = []
            hash_map[key].append(string)
        return list(hash_map.values())
        