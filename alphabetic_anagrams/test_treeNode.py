from unittest import TestCase

from alphabetic_anagrams import TreeNode


class TestTreeNode(TestCase):
    def test_push(self):
        test_cases = {
            'AB': ['A', [['B']]],
            'ABC': ['A', [['B'], ['C']]],
            'ABCD': ['A', [['B', [['D']]], ['C']]],
            '1234567890': ['1', [['2', [['4', [['6', [['8', [['0']]], ['9']]], ['7']]], ['5']]], ['3']]]
        }
        for input_data, output in test_cases.items():
            tree_root = TreeNode(input_data[0])
            for char in input_data[1:]:
                tree_root.push(TreeNode(char))
            actual_output = tree_root.get_as_list()
            self.assertEquals(output, actual_output)
