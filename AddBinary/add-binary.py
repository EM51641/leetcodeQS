'''
Time Complexity : O(log(N))
Space Complexity: O(N)

Approach:

We substract multiples of two at each bitwise iteration.
'''
import math


class Solution(object):

    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        summation = int(a, 2) + int(b, 2)  # sum_bin(a) +  sum_bin(b)

        if summation == 0:
            return '0'

        output = ''  # __SIZEOF_INT128__  in bits
        n = int(math.log(summation, 2))

        for x in range(n, -1, -1):
            if (summation >> x) >= 1:
                summation = summation - (1 << x)
                output = output + '1'
            else:
                output = output + '0'

        return output