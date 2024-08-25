class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # validate row
        for i in range(9):
            s = set()
            for j in range(9):
                if board[i][j] in s and board[i][j] != '.':
                    return False
                s.add(board[i][j])

        # validate col
        for i in range(9):
            s = set()
            for j in range(9):
                if board[j][i] in s and board[j][i] != '.':
                    return False
                s.add(board[j][i])

        # validate 3x3
        start = [(0, 0), (0, 3), (0, 6), (3, 0), (3, 3), (3, 6), (6, 0), (6, 3), (6, 6)]
        for i, j in start:
            s = set()
            for x in range(3):
                for y in range(3):
                    check = board[x + i][y + j]
                    if check in s:
                        return False
                    elif check != '.':
                        s.add(check)
        return True