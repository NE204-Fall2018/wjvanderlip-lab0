#!/usr/bin/env python3

import unittest
import pandas as pd
from pandas.util.testing import assert_series_equal
from unittest.mock import patch

import os
import sys

sys.path.append(os.path.abspath('../code'))  #this is a work around for an import issue I was having
import analysis, tools204


print('imports complete')

class TestBasicFuncs(unittest.TestCase):

    def setUp(self):
        pass

    print(analysis.get_change(2, 4))
    def test_get_change_equal(self):
        self.assertEqual(analysis.get_change(2, 2), 100.0)

    def test_get_change_firsthigh(self):
        self.assertEqual(analysis.get_change(2, 4), 50.0)

    def test_get_change_secondhigh(self):
        self.assertEqual(analysis.get_change(4, 2), 100.0)

    # def test_clean_up_sites_extra_spaces(self):
    #     self.assertEqual(analysis.clean_up_sites('1  3   4   5  2'), '1 3 4 5 2')
    #
    # def test_clean_up_sites_spacesandcommas(self):
    #     self.assertEqual(analysis.clean_up_sites('1,  3,   4  5,'), '1 3 4 5')
    #
    # def test_int_list(self):
    #     self.assertEqual(analysis.intList(['1','2', '3']), [0, 1, 2])
    #
    # def test_int_list_finds_duplicate_values(self):
    #     self.assertEqual(analysis.intList(['1','2', '2', '2', '4']), [0, 1, 3])

class TestTools(unittest.TestCase):

    def setUp(self):
        pass

    # def test_linear_calib(self):
    #     self.assertEqual(tools204.linear_calib([0, 0], [4, 4]), (1, 0, len(c) == 2048))
    #
    # def test_gammaEnergy(self):
    #     self.assertEqual(tools204.gammaEnergy('Cs137'), 661.something)

if __name__ == '__main__':
    unittest.main()
