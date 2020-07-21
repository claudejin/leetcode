# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        # trim heads
        while head and head.val == val:
            head = head.next
        
        # none is left
        if not head: return None
        
        # remove val
        prev_node, cur_node = head, head.next
        while cur_node:
            if cur_node.val == val:
                prev_node.next = cur_node = cur_node.next
            else:
                prev_node, cur_node = cur_node, cur_node.next
        
        return head