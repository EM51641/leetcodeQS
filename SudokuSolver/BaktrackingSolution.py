"""
TC: O(N * N^(N^2))
SC: O(N^N)
"""
class Solution:

    def solveSudoku(self, board):

        def isValid(row, col, ch):
    
            for i in range(9):
                    
                if board[i][col] == ch:
                    return False
                if board[row][i] == ch:
                    return False
                if board[3*(row//3) + i//3][3*(col//3) + i%3] == ch:
                    return False
            return True
    
        def backtracking(row, col):
            if row == 9:
                return True
    
            if board[row][col] == '.':
    
                for x in range(1, 10):
    
                    if isValid(row, col, str(x)) is True:
                        board[row][col] = str(x)
    
                        if col < 8 and backtracking(row, col + 1):
                            return True
                        elif col == 8 and backtracking(row + 1, 0):
                            return True
                        else:
                            board[row][col] = '.'
    
                return False
    
            else:
                if col < 8:
                    return backtracking(row, col + 1)
                else:
                    return backtracking(row + 1, 0) 

        backtracking(0, 0)   