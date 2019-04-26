###############################################################################
#           USAGE:
#               python3.7 permOfPal.py
#           DESCRIPTION:
#           1.5 Palindrome Permutation
#               Given a string, write a function to check if it is a
#               permutation of a palindrome. A palindrome is a word or phrase
#               that is the same forwards and backwards. A permutation is a
#               rearrangement of letters. The palindrome does not need
#               to be limited to just dictionary words.
#           Input:
#               string
#           Output:
#               boolean
# -----------------------------------------------------------------------------
# CREATED BY:   Deborah Perez
# VERSION:      20190426
###############################################################################
# 1.4 Palindrome Permutation: Given a string, write a
# function to check if it is a permutation of a palindrome.
# A palindrome is a word or phrase that is the same
# forwards and backwards. A permutation is a
# rearrangement of letters. The palindrome does not need
#  to be limited to just dictionary words.
# -----------------------------------------------------------------------------
import unittest
from collections import Counter

def isPermOfPal(string):

# If string is not of type str return false
    if type(string) is not str:
        return False

  # If length of string is less than or equal to 1 return False
    elif len(string) <= 1:
        return False

# All else
    else:
        # Remove all white spaces and make all lowercase letters
        string = string.replace(' ', '')
        string = string.lower()

        # Count all instances of each letter in the string using Counter()
        counter = Counter()
        for char in string:
          counter.update(char)

        # Check for odd number counts
        oddCount = 0
        for key in counter:
            value = counter[key]
            if value % 2 != 0:
              oddCount += 1
            else:
              continue

        # If there is only one letter with an odd number count or no letters with an odd number     # count, return True
        if oddCount <=1:
          return True
        #  If there is more than one letter with an odd number count, return False
        else:
          return False

class Test(unittest.TestCase):
  test_T = [('cato tac'), ('aA'), ('Balla b')]
  test_F = [([]), (''), (235)]

  def testPermOfPal(self):
    for testT in self.test_T:
      answer = isPermOfPal(testT)
      self.assertTrue(answer)
    for testF in self.test_F:
      answer = isPermOfPal(testF)
      self.assertFalse(answer)

if __name__ == "__main__":
    unittest.main()
    #print (isPermOfPal('cato tac'))
