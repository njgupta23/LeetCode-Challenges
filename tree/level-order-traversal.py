# Binary Tree Level Order Traversal

# Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

# For example:
# Given binary tree [3,9,20,null,null,15,7],
#     3
#    / \
#   9  20
#     /  \
#    15   7
# return its level order traversal as:
# [
#   [3],
#   [9,20],
#   [15,7]
# ]



# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def levelOrder(self, root):
    	if not root:
    		return []

    	order_dict = {}
    	self.dfs(root, order_dict, 0)

    	output = []
    	for lst in order_dict.values():
    		output.append(lst)

    	return output

    def dfs(self, node, d, level):
    	if level not in d:
    		d[level] = [node.val]
    	else:
    		d[level].append(node.val)

    	if node.left:
    		self.dfs(node.left, d, level + 1)
    	if node.right:
    		self.dfs(node.right, d, level + 1)
