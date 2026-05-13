class Solution:
    def dailyTemperatures(self, temps: List[int]) -> List[int]:
        res=[0]*len(temps)
        for i in range(len(temps)):
            curr=temps[i]
            for j in range(i+1,len(temps)):
                if temps[j] > curr:
                    res[i] = j-i
                    break
        return res
                
