# 993. Cousins in Binary Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        self.ans = False
        def helper(root, x, y):
            if not root:
                return 0
            elif root.val == x or root.val == y:
                return 1
            else:
                l = helper(root.left, x, y)
                r = helper(root.right, x, y)
                if l > 1 and r > 1:
                    self.ans = (l == r)
                rst = max(l, r)
            return rst + 1 if rst else 0
        helper(root, x, y)
        return self.ans
                