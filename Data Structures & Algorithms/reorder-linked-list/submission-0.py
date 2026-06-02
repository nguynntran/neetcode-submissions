# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head: return
        
        n = 0
        curr = head
        node_dict = {}

        while curr:
            node_dict[n] = curr
            n += 1
            curr = curr.next
        
        left, right = 0, n - 1
        while left < right:
            node_dict[left].next = node_dict[right]
            node_dict[right].next = node_dict[left + 1]
            left += 1
            right -= 1

        node_dict[left].next = None
                