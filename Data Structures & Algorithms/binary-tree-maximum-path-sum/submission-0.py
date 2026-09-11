# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        maximum = float("-inf")

        def dfs(node):

            nonlocal maximum

            if node is None:
                return 0

            left_gain = dfs(node.left)
            right_gain = dfs(node.right)

            left_gain = max(left_gain, 0)
            right_gain = max(right_gain, 0)

            current_value = node.val + left_gain + right_gain

            maximum = max(maximum, current_value)

            return node.val + max(left_gain, right_gain)

        dfs(root)

        return maximum
        