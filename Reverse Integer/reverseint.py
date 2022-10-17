class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """

        string = str(x)

        if '-' in string:
            # Explanation:
            # 4 bytes signed integer goes from :
            # 0b100000000000000000000000000000000
            neutralnb = '2147483648'
            string = string.replace('-', '')
            revstr = string[::-1].lstrip('0')
            is_neg = True

        else:
            # To:
            # 0b011111111111111111111111111111111
            neutralnb = '2147483647'
            revstr = string[::-1].lstrip('0')
            is_neg = False

        if len(revstr) > 10 or revstr == '':
            return 0

        if len(revstr) == 10:

            for j, char in enumerate(neutralnb):
                if int(char) < int(revstr[j]):
                    return 0

                elif int(char) == int(revstr[j]):
                    pass

                else:
                    break

        if is_neg:
            revstr = '-' + revstr

        return revstr
