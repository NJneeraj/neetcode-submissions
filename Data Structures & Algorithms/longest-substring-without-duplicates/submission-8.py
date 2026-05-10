class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) < 2:
            return len(s)
        i=0
        seen=set()
        max_len=0
        curr=0
        last_ind=0
        while i < len(s):
            if s[i] in seen:
                max_len=max(curr,max_len)
                curr=0
                seen.clear()
                last_ind+=1
                i=last_ind
            else:
                seen.add(s[i])
                curr+=1
                i+=1

        return max(max_len,curr)
