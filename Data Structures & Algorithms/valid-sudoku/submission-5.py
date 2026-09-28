class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row, square, col = defaultdict(set), defaultdict(set), defaultdict(set)

        def isValid(r, c):
            val = board[r][c]

            if val in row[r]:
                return False
            
            if val in col[c]:
                return False
            
            if val in square[(r // 3, c // 3)]:
                return False
            
            return True
        
        for r in range(9):
            for c in range(9):
                if board[r][c] != ".":
                    val = board[r][c]

                    if isValid(r, c):
                        row[r].add(val)
                        col[c].add(val)
                        square[(r//3, c//3)].add(val)
                    else:
                        return False
        return True
                

