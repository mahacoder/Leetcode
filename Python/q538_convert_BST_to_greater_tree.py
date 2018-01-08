# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        self.convert(root, 0)
        return root

    def convert(self, node, toadd):
        subtreesum = 0
        if node==None:
            return subtreesum

        subtreesum += self.convert(node.right, toadd)
        nodeval = node.val
        node.val += toadd + subtreesum
        subtreesum += self.convert(node.left, node.val)
        subtreesum += nodeval
        return subtreesum
        
