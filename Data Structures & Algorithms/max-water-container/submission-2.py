class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area=0
        i,j=0,len(heights)-1
        while i < j:
            area= (j-i) * min(heights[i] ,heights[j])
            if heights[i] < heights[j]:
                i+=1
            else : 
                j-=1
            max_area =max(max_area,area)
        return max_area