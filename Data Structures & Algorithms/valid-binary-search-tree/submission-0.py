# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def valid(node, lower, higher):

            if node is None:
                return True

            if not (lower < node.val < higher):
                return False

            left_valid = valid(node.left, lower, node.val)

            right_valid = valid(node.right, node.val, higher)

            return left_valid and right_valid

        return valid(root, float("-inf"), float("inf"))


        