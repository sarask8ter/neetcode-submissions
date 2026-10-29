# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        res = dummy

        cur1, cur2 = l1, l2
        carry = 0

        while cur1 or cur2:
            val1 = cur1.val if cur1 else 0
            val2 = cur2.val if cur2 else 0

            sm = val1 + val2 + carry

            if sm > 9:
                carry = 1
                sm %= 10
            else:
                carry = 0
            
            res.next = ListNode(sm)
            res = res.next

            if cur1:
                cur1 = cur1.next
            
            if cur2:
                cur2 = cur2.next
        
        if carry:
            res.next = ListNode(1)
            res = res.next
        
        return dummy.next




