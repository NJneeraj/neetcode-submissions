class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        res = [0]*26
        for ch in s:
            res[ord(ch)-ord('a')] +=1
        for ch in t:
            res[ord(ch)-ord('a')] -=1
        if res == [0]*26:
            return True


        return False
        