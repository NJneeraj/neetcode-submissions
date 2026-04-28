class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded=""
        for s in strs:
            encoded = encoded + str(len(s))+'#'+ s
        return encoded

    def decode(self,s:str)->List[str]:
        s_len = len(s)
        strs=[]
        i=0
        while i < s_len:
            j=i
            while s[j]!="#" and j < s_len -1:
                j = j+1
            num_str = s[i:j]
            is_valid_num = num_str.isnumeric()
            if is_valid_num:
                str_len = int(num_str)
                strs.append(s[i+len(num_str) +1:str_len + i+len(num_str) +1])
                i  = str_len+i + 1 + len(num_str)
            else:
                i=i+1
            
        return strs