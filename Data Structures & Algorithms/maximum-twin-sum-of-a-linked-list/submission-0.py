# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        l = []
        tail = head
        while tail != None:
            l.append(tail.val)
            tail=tail.next
        

        reversed_l = l[::-1]

        sum_l = [l[i] + reversed_l[i] for i in range(len(l))]
        return max(sum_l)