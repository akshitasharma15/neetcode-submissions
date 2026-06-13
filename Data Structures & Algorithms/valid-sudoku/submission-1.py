class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        set_row= defaultdict(set)
        set_col = defaultdict(set)
        sq_set = defaultdict(set)

        for i in range(len(board)):
            for j in range(len(board)):
                val = board[i][j]
                if val == ".":
                    continue
                if val in sq_set[((i//3) * 3  + (j//3))] or val in set_row[i] or val in set_col[j]:
                    return False
                
                sq_set[((i//3) * 3  + (j//3))].add(val)
                set_row[i].add(val)
                set_col[j].add(val)

        return True