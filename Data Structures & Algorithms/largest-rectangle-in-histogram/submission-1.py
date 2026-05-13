class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        if not heights:
            return 0
        max_area = heights[0] 
        for i in range(len(heights)):
            min_height = heights[i]  # 2 , 1 , 3
            for j in range(i + 1, len(heights)):
                min_height = min(heights[j], min_height)
                curr_ind_max = max(min_height * (j - i + 1), heights[j])
                max_area = max(max_area, curr_ind_max)

        return max_area
