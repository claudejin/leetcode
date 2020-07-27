# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if len(postorder) == 0: return None
        if len(postorder) == 1: return TreeNode(postorder[0])
        
        root_val = postorder[-1]
        left_len = inorder.index(root_val)
        
        root_node = TreeNode(root_val,
            self.buildTree(inorder[:left_len], postorder[:left_len]),
            self.buildTree(inorder[left_len+1:], postorder[left_len:len(postorder)-1]))
        
        return root_node
