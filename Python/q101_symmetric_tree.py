# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        def check(left, right):
            if left is None and right is None:
                return True
            elif left is not None and right is not None and left.val==right.val:
                return check(left.left, right.right) and check(left.right, right.left)
            else: return False

        return check(root, root)
