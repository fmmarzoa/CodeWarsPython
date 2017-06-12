from itertools import permutations

from unittest import TestCase

from alphabetic_anagrams import list_position, build_tree


class TestListPosition(TestCase):
    # def test_list_position(self):
    #     print(list_position("BAAA"))
    #     self.fail()

    def test_build_tree(self):
        tree = build_tree('QUESTION')
        print(tree)
        if not tree:
            self.fail()
