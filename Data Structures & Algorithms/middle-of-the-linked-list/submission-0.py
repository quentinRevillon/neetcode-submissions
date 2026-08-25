# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        values = []
        node = head
        val = node.val
        next_node = node.next
        values.append(node)

        while next_node != None:
            node = next_node
            values.append(node)
            next_node = node.next
            
        return values[len(values)//2]
