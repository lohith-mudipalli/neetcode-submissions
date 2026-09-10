# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        if root is None:
            return False

        if self.isSametree(root, subRoot):
            return True
        
        left_node = self.isSubtree(root.left, subRoot)
        right_node = self.isSubtree(root.right, subRoot)

        return left_node or right_node


    def isSametree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        if root is None and subRoot is None:
            return True

        if root is None or subRoot is None:
            return False

        if root.val != subRoot.val:
            return False

        
        left_same = self.isSametree(root.left, subRoot.left)
        right_same = self.isSametree(root.right, subRoot.right)

        return left_same and right_same
        