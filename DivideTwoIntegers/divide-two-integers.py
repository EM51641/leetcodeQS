class Solution(object):
    def divide(self, A, B):

        if (A == -2147483648 and B == -1):
            return 2147483647

        divided = abs(A)
        divisor = abs(B)

        multi = 0
        output = 0

        while divided >= divisor:
            multi = 1
            temp = divisor

            while divided >= temp:
                divided = divided - temp
                output = output + multi
                multi = multi + multi

                if temp >> 30 < 1:
                    temp = temp + temp
                    break

        if (A < 0 and B > 0) or (A > 0 and B < 0):
            output = - output

        else:
            output = output

        return output
