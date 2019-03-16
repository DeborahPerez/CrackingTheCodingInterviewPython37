###############################################################################
#           USAGE:
#               python3.7 isUnique.py
#           DESCRIPTION:
#               Attempt to connect to NETAPP server through HTTPS for C-mode
#               (Cluster-mode) or 7-mode, make appropriate snap mirror API
#               calls to the NAS Array, save API call results as an xml file,
#               parse xml file for desired attributes, and save to a csv file
#           Input:
#               String
#           Output:
#               Boolean
# -----------------------------------------------------------------------------
# CREATED BY:   Deborah Perez
# VERSION:      20190315
###############################################################################
# 1.1 Is Unique
# Implement an algorithm to determine if a string has all unique
# characters.

# Comment the section below to test the solution without additional data
# structures
###############################################################################
import unittest
from collections import Counter

def isUnique(string):
    if len(string) > 128:
        return False
    c = Counter()
    for char in string:
        c.update(char)
        if c[char] > 1:
            return False
    return True
###############################################################################

# What if you cannot use additional data structures?
# Comment the above block and uncomment the block below to test the solutions
# without additional data structures
###############################################################################
# import unittest
#
# def isUnique(string):
#     if len(string) > 128:
#         return False
#
#     uniqueList = []
#     for char in string:
#         ordChar = ord(char)
#         if ordChar in uniqueList:
#             return False
#         uniqueList.append(ordChar)
#     return True
###############################################################################

class Test(unittest.TestCase):
    test_T = [('abcdefg'), ('5679asdf'), (' ')]
    test_F = [('dsadsadafasfsa'), ('dsadsa356u7hhaaa'), ('#$%^fdsfs##$')]

    def test_unique(self):
        for test in self.test_T:
            answer = isUnique(test)
            self.assertTrue(answer)

        for test in self.test_F:
            answer = isUnique(test)
            self.assertFalse(answer)

if __name__ == "__main__":
    unittest.main()
