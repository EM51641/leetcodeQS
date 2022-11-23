"""
K: Average Number of elements for each list in a map
Time complexity: O(KN^2/2) -> O(N^2)
Space complexity: O(KN + K^N + 9*k) -> O(K^N)
"""

import collections


class Solution(object):
    mapping = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z'],
        }

    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """

        def recursion(
                stack, stack_remaining):

            if not stack_remaining:
                return stack

            new_stack = collections.deque()
            rem = stack_remaining.popleft()

            for original in stack:
                for schar in rem:
                    new_stack.append(original + schar)

            return recursion(new_stack, stack_remaining)

        all_lsts = collections.deque()

        for i in digits:
            all_lsts.append(self.mapping[i])

        if len(all_lsts) > 0:
            res = recursion(all_lsts.popleft(), all_lsts)
            return res
        else:
            return all_lsts
