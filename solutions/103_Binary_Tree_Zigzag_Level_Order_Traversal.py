# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root: return []

        res = []
        children, ltor = [root], True
        while len(children) > 0:
            res.append([node.val for node in (children if ltor else reversed(children))])

            next_children = []
            for node in children:
                if node.left: next_children.append(node.left)
                if node.right: next_children.append(node.right)

            children, ltor = next_children, not ltor

        return res

