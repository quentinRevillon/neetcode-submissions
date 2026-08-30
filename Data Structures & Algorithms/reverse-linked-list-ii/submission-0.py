# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:

        vals = []

        while head.next != None:
            next_node = head.next
            vals.append(head.val)
            head = next_node
        next_node = head.next
        vals.append(head.val)


        new_vals = []
        for i, val in enumerate(vals):
            if i+1<left or i+1>right:
                new_vals.append(val)
            elif left<=i+1<=right:
                new_vals.append(vals[right-(i+1-left)-1])
            print(val)

        print(new_vals)

        r=ListNode(new_vals[0])
        node = r

        for i, val in enumerate(new_vals[1:]):
            node.next = ListNode(val)
            node = node.next

        return r
            


            


   