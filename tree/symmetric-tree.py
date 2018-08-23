# Symmetric Tree

# Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

# For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

#     1
#    / \
#   2   2
#  / \ / \
# 3  4 4  3
# But the following [1,2,2,null,3,null,3] is not:
#     1
#    / \
#   2   2
#    \   \
#    3    3


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def isSymmetric(self, root):
        if root is None:
            return True
        else:
            return self.isMirror(root, root)
    
    def isMirror(self, Lroot, Rroot):
        if Lroot is None and Rroot is None:
            return True
        if Lroot is None or Rroot is None:
            return False
        
        if Lroot.val == Rroot.val:
        	# check if left root's left subtree is mirror of right root's right subtree
            outer = self.isMirror(Lroot.left, Rroot.right)
            # check if left root's right subtree is mirror of right root's left subtree
            inner = self.isMirror(Lroot.right, Rroot.left)
            # should return True if they are mirror images
            return (outer and inner)
        else:
            return False

