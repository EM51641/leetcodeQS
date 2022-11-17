"""
a: number of words
b: length of words
c: set of words

Time Complexity: O((N * c - a * b) *  a * b + N) -> O(N)

We iterate over N - a * b
We subiterate through words (Complexity O(a))
And select a substring (Complexity O(b)).

Space Complexity: O(a + b)

substring of length b and the
dictionary where a keys are sotred

"""
import collections


class Solution(object):

    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """

        str_lgth = len(s)
        sgl_length = len(words[0])
        n_word = len(words)
        word_count = collections.Counter(words)

        substring = sgl_length * n_word
        returned_list = []

        r = 0
        while r <= str_lgth - substring:
            rem = word_count.copy()
            wc = 0

            for i in range(r, r + substring, sgl_length):
                sub = s[i: i + sgl_length]
                if rem[sub] > 0:
                    rem[sub] = rem[sub] - 1
                    wc = wc + 1
                else:
                    break

            if wc == n_word:
                returned_list.append(r)

            r = r + 1

        return returned_list
