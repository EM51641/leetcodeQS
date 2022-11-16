"""
Time Complexity:

O((N + 2) * N! + N!) -> O(N * N!)

Why the +2?
We remove and append from respectively the set
/stack at each iteration

Why the +N!?

We check whether our set is empty at the end
of each recursion

Space Complexity:


O(N! + 2*N)


From where does the 3*N arises?

first N: We transform our first list into a set

Second N: For each subtree as we go branch by branch we
copy what is left from the original set and what we currently
have on the stack.
"""

import copy


class Solution(object):

    def backtracking(self, set_, att_list, nlist):

        if len(set_) == 0:
            nlist.append(att_list)

        for x in set_:
            used_set = set_.copy()
            new_list = copy.copy(att_list)
            new_list.append(x)
            used_set.remove(x)
            self.backtracking(used_set, new_list, nlist)

    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        nset = set(nums)
        nlist = []

        for x in nset:
            att_list = []
            used_set = nset.copy()
            att_list.append(x)
            used_set.remove(x)
            self.backtracking(used_set, att_list, nlist)

        return nlist
