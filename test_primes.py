#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      mmk
#
# Created:     04/11/2018
# Copyright:   (c) mmk 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import unittest

from testing_ci import is_prime

class PrimesTestCase(unittest.TestCase):
    """Tests for `primes.py`."""

    def test_is_five_prime(self):
        """Is five successfully determined to be prime?"""
        self.assertTrue(is_prime(5))

if __name__ == '__main__':
     unittest.main()
