class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        s_map = {}
        for char in s:
            s_map[char] =(s_map.get(char) or 0) + 1
        t_map = {}
        for char in t:
            t_map[char] =(t_map.get(char) or 0) + 1
        for x in s_map:
            if s_map.get(x) != t_map.get(x):
                return False
        return True
        