"""
Given during an interview with Bloomberg.

Given a tree such as:

         212
       /  |  \
    421   3  89
    /       /   \
   32     16     44

Write a function that takes in two values and determines if the second paramter is a descendant node of the first parameter.
Example 1
solution.solve(89, 16) = true
Example 2
solution.solve(412, 44) = false
"""


class Node:
    def __init__(self, val: int, children: list = None):
        self.val = val
        if children:
            self.children = children
        else:
            self.children = []

    def is_leaf(self):
        return len(self.children) == 0


'''
Build the tree
         212
       /  |  \
    421   3  89
    /       /   \
   32     16     44
'''
tree = Node(212, [Node(421, [Node(32)]), Node(3),
                  Node(89, [Node(16), Node(44)])])


class Solution:
    def solve(self, node: Node, parent: int, descendant: int):
        ''' Find the parent node first since it would have to be higher up in the tree. '''
        parent = self.find_node(node, parent)
        if not parent:
            return False

        ''' If the parent is found, just search from that node down. No need to search the other nodes of the Tree. '''
        child = self.find_node(parent, descendant)
        if child:
            return True

        ''' Child was not found in parent's descendants. '''
        return False

    def find_node(self, node: Node, val: int):
        if node.val == val:
            return node
        elif not node.is_leaf():
            for c in node.children:
                found = self.find_node(c, val)
                if found:
                    return found
        return None


''' pytest '''
solution = Solution()
'''
Tree
         212
       /  |  \
    421   3  89
    /       /   \
   32     16     44
'''


def test_case_212_421():
    assert solution.solve(tree, 212, 421) == True


'''
Tree
         212
       /  |  \
    421   3  89
    /       /   \
   32     16     44
'''


def test_case_212_3():
    assert solution.solve(tree, 212, 3) == True


'''
Tree
         212
       /  |  \
    421   3  89
    /       /   \
   32     16     44
'''


def test_case_212_89():
    assert solution.solve(tree, 212, 89) == True


'''
Tree
         212
       /  |  \
    421   3  89
    /       /   \
   32     16     44
'''


def test_case_212_32():
    assert solution.solve(tree, 212, 32) == True


'''
Tree
         212
       /  |  \
    421   3  89
    /       /   \
   32     16     44
'''


def test_case_212_16():
    assert solution.solve(tree, 212, 16) == True


'''
Tree
         212
       /  |  \
    421   3  89
    /       /   \
   32     16     44
'''


def test_case_212_44():
    assert solution.solve(tree, 212, 44) == True


'''
Tree
         212
       /  |  \
    421   3  89
    /       /   \
   32     16     44
'''


def test_case_421_32():
    assert solution.solve(tree, 421, 32) == True


'''
Tree
         212
       /  |  \
    421   3  89
    /       /   \
   32     16     44
'''


def test_case_89_16():
    assert solution.solve(tree, 89, 16) == True


'''
Tree
         212
       /  |  \
    421   3  89
    /       /   \
   32     16     44
'''


def test_case_89_44():
    assert solution.solve(tree, 89, 44) == True


'''
Tree
         212
       /  |  \
    421   3  89
    /       /   \
   32     16     44
'''


def test_case_89_32():
    assert solution.solve(tree, 89, 32) == False


'''
Tree
         212
       /  |  \
    421   3  89
    /       /   \
   32     16     44
'''


def test_case_16_421():
    assert solution.solve(tree, 16, 421) == False


'''
Tree
         212
       /  |  \
    421   3  89
    /       /   \
   32     16     44
'''


def test_case_44_3():
    assert solution.solve(tree, 44, 3) == False


'''
Tree
         212
       /  |  \
    421   3  89
    /       /   \
   32     16     44
'''


def test_case_44_421():
    assert solution.solve(tree, 44, 421) == False


'''
Tree
         212
       /  |  \
    421   3  89
    /       /   \
   32     16     44
'''


def test_case_3_no_children():
    assert solution.solve(tree, 3, 421) == False


'''
Tree
         212
       /  |  \
    421   3  89
    /       /   \
   32     16     44
'''


def test_case_no_such_parent():
    assert solution.solve(tree, 500, 89) == False


'''
Tree
         212
       /  |  \
    421   3  89
    /       /   \
   32     16     44
'''


def test_case_no_such_child():
    assert solution.solve(tree, 89, 500) == False
