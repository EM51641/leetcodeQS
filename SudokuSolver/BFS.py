"""
Sudoku Solver Using DFS

k: total number of index prefiled
m: length of the limit set

Time Complexity: O(2N * N^(N^2 - k) + N^2) -> O(2N * N^(N^2 - k))

Why O(2N * N^(N^2 - k)) ?

We iterate N fold when we have a blank to check the values except
when a value is already assigned to it.

Why + N^2?

We add N^2 because at the beginning we pre-check the whole figure
to lower the number of trees we will draw through the dfs.

Why multipling by 2N:

2 copied lists

Space Complexity: O(N^4) = O(h * (2N^2) ) where w is of
the order (N + 1)!/N -1
"""


import copy
import collections


class Solution(object):

    def solveSudoku(self, board):

        nset = set()
        for i in range(0, 9):
            for j in range(0, 9):
                if board[i][j] != '.':
                    nset.add((i, board[i][j]))
                    nset.add((board[i][j], j))
                    nset.add((i//3, j//3, board[i][j]))

        nboard = self.dfs(0, 0, board, nset, list())

        for x in range(0, len(board)):
            board[x] = nboard[x * len(board): (x + 1) * len(board)]

    def dfs(self, idx, col, board, nset, lst):

        queue = collections.deque([(idx, col, board, nset, lst)])

        while len(queue) > 0:

            idx, col, board, nset, lst = queue.popleft()

            if board[idx][col] == '.':

                for x in (
                        u'1', u'2', u'3', u'4', u'5', u'6', u'7',
                        u'8', u'9'):

                    if (idx, x) in nset or (x, col) in nset or (
                         idx//3, col//3, x) in nset:
                        continue

                    else:
                        new_nset = copy.copy(nset)
                        new_lst = copy.copy(lst)
                        new_nset.add((idx, x))
                        new_nset.add((x, col))
                        new_nset.add((idx//3, col//3, x))
                        new_lst.append(x)

                        if col < 8:
                            queue.append(
                                (idx, col + 1, board, new_nset, new_lst))
                        elif col == 8 and idx < 8:
                            queue.append(
                                (idx + 1, 0, board, new_nset, new_lst))
                        else:
                            return new_lst

            else:

                lst.append(board[idx][col])

                if col < 8:
                    queue.append((idx, col + 1, board, nset, lst))
                elif col == 8 and idx < 8:
                    queue.append((idx + 1, 0, board, nset, lst))
                else:
                    return lst
