# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:

        slow, fast = head, head.next
        while fast.next:
            slow, fast = slow.next, fast.next.next

        tail = slow.next
        def reverse(head: ListNode):
            prev = None
            node = head
            while node:
                next_node = node.next
                node.next = prev
                prev = node
                node = next_node
            return prev
        
        reversed_tail = reverse(tail)
        # print(reversed_tail.val, reversed_tail.next.val)
        res = 0
        while reversed_tail:
            res = max(res, head.val + reversed_tail.val)
            head = head.next
            reversed_tail = reversed_tail.next
            

        return res

