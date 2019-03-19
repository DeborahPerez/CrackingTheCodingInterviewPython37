###############################################################################
#           USAGE:
#               python3.7 URLify.py
#           DESCRIPTION:
#           1.3 URLify
#               Write a method to replace all spaces in a string
#               with '%20: You may assume that the string has
#               sufficient space at the end to hold the additional
#               characters, and that you are given the "true" length of
#               the string.
#           Input:
#               string
#           Output:
#               newString or None
# -----------------------------------------------------------------------------
# CREATED BY:   Deborah Perez
# VERSION:      20190318
###############################################################################
# 1.3 URLify
# Write a method to replace all spaces in a string
# with '%20: You may assume that the string has
# sufficient space at the end to hold the additional
# characters, and that you are given the "true" length of
# the string.
###############################################################################
import unittest

def URLify(string):
    rep = '%20'
    if type(string) == str and len(string) > 0:
        newString = string.replace(' ', rep)
        return newString

    else:
        print ('Not a string!')
        return None

class Unittest(unittest.TestCase):
    test_T = (['as 20 ', 'as%2020%20'], ['   ', '%20%20%20'], ['hello', 'hello'])

    test_F = ([244, 7676], [000, 000], [123, 1])

    def test_URLify(self):
        for test in self.test_T:
            results = URLify(test[0])
            if results == test[1]:
                answer = True
            else:
                answer = False
            self.assertTrue(answer)

        for test in self.test_F:
            results = URLify(test[0])
            if results == None:
                answer = False
            else:
                answer = True
            self.assertFalse(answer)

if __name__ == '__main__':
    unittest.main()
