# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        if not head or not head.next:
            return False

        node1 = head
        node2 = head.next

        while node1 != node2:
            if node1.next:
                node1 = node1.next
            else:
                return False
            
            if node2.next and node2.next.next:
                node2 = node2.next.next
            else:
                return False
        
        return True
        