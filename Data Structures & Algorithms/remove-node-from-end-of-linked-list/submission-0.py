# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        N = 0
        while curr:
            curr = curr.next
            N += 1
        
        if N - n == 0:
            return head.next
        else:
            first = head 
            idx = 0
            while idx < (N - n - 1):
                first = first.next
                idx += 1
            first.next = first.next.next

        return head

