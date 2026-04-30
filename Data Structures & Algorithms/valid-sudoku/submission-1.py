import math
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen=set()
        for i in range(9):
            for j in range(9):
                val = board[i][j]
                if val==".":
                    continue
                box = (i//3,j//3)
                row_key = (val,"row",i)
                col_key = (val,"col",j)
                box_key = (val,"box",box)
                if row_key in seen or col_key in seen or box_key in seen: 
                    return False
                seen.add(row_key)
                seen.add(col_key)
                seen.add(box_key)
        return True

                    

               