###############################################################################
#           USAGE:
#               python3.7 checkPermuation.py
#           DESCRIPTION:
#           1.2 Check Permutation
#               Implement algorithm to determine if a string is a permutation
#               of another string
#           Input:
#               string1, string2
#           Output:
#               Boolean
# -----------------------------------------------------------------------------
# CREATED BY:   Deborah Perez
# VERSION:      20190317
###############################################################################
# 1.2 isPermutation
# Implement algorithm to determine if a string is a permutation
# of another string
###############################################################################

import unittest
from collections import Counter

def check_permutation(string1, string2):
    if type(string1) is not str or type(string2) is not str:
        return False
    if len(string1) != len(string2):
        return False

    c1 = Counter()
    for char1 in string1:
        c1.update(char1)
    c2 = Counter()
    for char2 in string2:
        c2.update(char2)

    if c1 == c2:
        return True
    else:
        return False

class Unittest(unittest.TestCase):
    test_T = (["abc", "bca"], ["scram", "crams"], ["x", "x"])
    test_F = (["adsadsad", "ddsad"], [123, "xyz"], ["wert", "0987"])

    def test_permutation(self):
        for test in self.test_T:
            answer = check_permutation(test[0], test[1])
            self.assertTrue(answer)
        for test in self.test_F:
            answer = check_permutation(test[0], test[1])
            self.assertFalse(answer)

if __name__ == "__main__":
    unittest.main()
