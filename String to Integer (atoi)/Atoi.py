"""
Time complexity -> O(N) : At most we go through the whole string
Space complexity -> O(1) : we only use the served string

We only allow ourselves to use 32 bits
integers in our algorithm
"""


class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """

        number = 0

        MAX_INTEGER = 2147483647
        MIN_INTEGER = -2147483648

        sign = 1
        val = EXTREME_VAL = MAX_INTEGER

        signed = False
        int_began = False

        for i, char in enumerate(s):

            if not char.isdigit():

                if (char in ('-', '+') and signed is False
                        and int_began is False):

                    signed = True
                    if char == '-':
                        sign = - 1
                        val = EXTREME_VAL = MIN_INTEGER

                elif (
                    char in ('-', '+') and (
                        signed is not True and int_began is not True)
                ):
                    pass

                elif (char in (' ') and int_began is False
                        and signed is not True):
                    pass

                else:
                    return number

            if char.isdigit():

                if char == '0' and number == 0:
                    if int_began is False:
                        int_began = True
                    if signed is False:
                        signed = True
                    else:
                        continue

                if sign == -1 and val < -1:
                    if int_began is False:
                        int_began = True
                        signed = True

                    val = int(val/10)

                elif sign == 1 and val > 0:
                    if int_began is False:
                        int_began = True
                        signed = True
                    val = int(val/10)

                if val == 0 or val == -1:

                    if len(s) - 1 > i and s[i + 1].isdigit():
                        return EXTREME_VAL

                    elif sign == 1:

                        if number > int(EXTREME_VAL/10):
                            return EXTREME_VAL

                        elif number == int(EXTREME_VAL/10) and int(char) > 7:
                            return EXTREME_VAL

                        else:
                            number = number * 10 + int(char)
                            break

                    elif sign == -1:

                        if number - 1 < int(EXTREME_VAL/10):
                            return EXTREME_VAL

                        # - 1 is added because Python rounds to the lower
                        # integer
                        elif (number - 1 == int(EXTREME_VAL/10)
                                and int(char) > 8):
                            return EXTREME_VAL

                        else:
                            number = number * 10 - int(char)
                            break
                else:
                    number = number * 10 + sign * int(char)

        return number
