class Solution(object):
    def isMatch(self, s, p):
        #TOP DOWN  Memoization
        """
        :type s: str
        :type p: str
        :rtype: bool
        """

        def dfs(i, j):

            if i >= len(s) and j >= len(p):
                return True

            if j >= len(p):
                return False


            match = ( i < len(s)) and (s[i] == p[j] or p[j] == '.')

            if (j + 1) < len(p) and p[j + 1] == "*":
                return (dfs(i, j + 2) | (match and dfs(i + 1, j)))


            if match:
                return dfs(i+1, j+1)

            return False


        return dfs(0, 0)              

















       # def recursion_loop(s, p):

