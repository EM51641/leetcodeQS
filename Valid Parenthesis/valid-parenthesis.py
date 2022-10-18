'''
Time complexity: O(n) -> We iterate through the string.
Space complexity: O(n) -> Worst case scenario -> Ex: '(((((('.
'''


class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        if len(s) % 2 != 0:
            return False

        stack = []
        dct = {'{': '}', '(': ')', '[': ']'}
        j = 0

        while j < len(s):
            char = s[j]

            if char in ('(', '[', '{'):
                stack.append(char)

            if char in (')', ']', '}'):
                if len(stack) > 0 and dct[stack[-1]] == char:
                    stack.pop()

                else:
                    return False

            j = j + 1

        return (len(stack) == 0)

