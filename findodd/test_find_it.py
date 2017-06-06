from unittest import TestCase
from FindTheOddInt import find_it


class TestFindIt(TestCase):
    def test_find_it(self):
        self.assertEquals(find_it([20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5]), 5)
