# https://www.codewars.com/kata/alphabetic-anagrams/python


class TreeNode:
    """A node for managing a binary tree of characters."""
    char = None
    left = None
    right = None

    def __init__(self, char):
        self.char = char

    def __str__(self):
        return self.to_string()

    def to_string(self, depth=0):
        rtn = self.char
        depth += 1
        if self.left:
            rtn += "\n" + (" " * depth) + "+" + str(self.left.to_string(depth))
            if self.right:
                rtn += "\n" + (" " * depth) + "+" + str(self.right.to_string(depth)) + "\n"
        return rtn

    def get_as_list(self):
        siblings = []
        if self.left:
            left_side = self.left.get_as_list()
            if left_side:
                siblings.append(left_side)
            if self.right:
                right_side = self.right.get_as_list()
                if right_side:
                    siblings.append(right_side)
        if siblings:
            return [self.char, siblings]
        else:
            return [self.char]

    def push(self, new_node):
        """Adds a new node to the tree. It will try first to allocate
        it in self node, and if it is complete, will go for the left
        node recursively"""
        if self.left is None:
            self.left = new_node
        elif self.right is None:
            self.right = new_node
        else:
            # Node is full, so ask the left node to find space
            self.left.push(new_node)
        return new_node


def list_position(word):
    """Return the anagram list position of the word"""
    if not word:
        return -1  # Empty word
    # Create a tree of chars
    chars = sorted(word)
    tree = build_tree(chars)
    return -1


def build_tree(chars, char_index=0):
    if not chars:
        return None  # No more chars
    tree_node = TreeNode(chars[char_index])
    left_chars = list(chars)
    del (left_chars[char_index])
    if left_chars:
        tree_node.push(build_tree(left_chars))
        if char_index < len(chars) - 1:
            char_index += 1
            tree_node.push(build_tree(chars, char_index))
    return tree_node
