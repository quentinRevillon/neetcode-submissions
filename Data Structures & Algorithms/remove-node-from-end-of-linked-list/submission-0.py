# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        def util(head,n):
            if head.next:
                head.next, s = util(head.next, n)
                s+=1
            else:
                s=1

            if s==n+1:
                head.next = head.next.next
            

            return head, s
        dummy_head = ListNode(None, head)
        head, s = util(dummy_head, n)
        return head.next
        