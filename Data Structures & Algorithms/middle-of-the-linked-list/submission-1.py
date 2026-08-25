# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = head
        s=1
        while node.next:
            s+=1
            node = node.next
        mid = s//2
        node = head
        for j in range(mid):
            node = node.next
        
        return node
