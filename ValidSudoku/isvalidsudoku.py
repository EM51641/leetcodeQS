"""

Time Complexity:

O((N/3)^6) -> O(N^6):

We run first through 2 nested loop
with a length of N/3 (last integer is excluded and
we begin by 0) each.

Then we create a sublist of N/3 for N/3 times

Then we iterate point by point through
this N/3 * N/3 matrix.

Space Complexity:

O(9N + N^2/3) -> O(N^2)

Creating of the temporary set: O(N^2/3) at worst
Storing all the numbers given the strict Sudoku
rules (We need to not the same number more than
once for any column): O(9 * N)
"""
import collections


class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        dct = collections.defaultdict(list)
        for x, y in zip(
                range(0, len(board) - 2, 3), range(3, len(board) + 1, 3)
                ):
            for z, m in zip(
                 range(0, len(board) - 2, 3), range(3, len(board) + 1, 3)
                 ):

                sublist = [lst[z:m] for lst in board[x:y]]
                new_set = set()

                for i, nlist in enumerate(sublist):
                    for j, char in enumerate(nlist):
                        if char != '.':

                            if m in dct.get(
                                'row%i' % (i+x), []) or m in dct.get(
                                    'col%i' % (j+z), []):
                                return False

                            else:
                                dct['row%i' % (i+x)].append(m)
                                dct['col%i' % (j+z)].append(m)

                            if m not in new_set:
                                new_set.add(m)
                            else:
                                return False
        return True
