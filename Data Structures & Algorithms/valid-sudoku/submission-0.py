import math
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        r_map = {}
        c_map={}
        b_map={}
        for i in range(9):
            for j in range(9):
                val = board[i][j]
                if val==".":
                    continue
                else:
                    curr_row = r_map.get(i,set())
                    curr_col = c_map.get(j,set())
                    box_i = math.floor(i/3)
                    box_j = math.floor(j/3)
                    curr_box = b_map.get((box_i,box_j),set())
                    if val in curr_row or val in curr_col or val in curr_box:
                        return False
                    curr_row.add(val)
                    r_map[i] = curr_row
                    curr_col.add(val)
                    c_map[j] = curr_col
                    curr_box.add(val)
                    b_map[(box_i,box_j)] = curr_box
        print(r_map,"\n")
        print(c_map,"\n")
        print(b_map,"\n")
        return True

                    

               