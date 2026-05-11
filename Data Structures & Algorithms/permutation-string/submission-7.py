from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # we need to find any substring in s2 that contains the characters of s1
        # in any order
        if len(s1)> len(s2):
            return False
        c1 = Counter(s1)
        l,r = 0,len(s1)-1
        count_perm = {}
        
        while r < len(s2):
            print(s2[l:r+1])
            if c1== Counter(s2[l:r+1]):
                return True
            else:
                l+=1
                r+=1
        return False

            
            
            
        
        
                
        return False
