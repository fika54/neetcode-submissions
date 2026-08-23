# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        cur = head

        l = None

        while cur != None:
            n = cur.next

            cur.next = l

            l = cur

            cur = n

        return l


        