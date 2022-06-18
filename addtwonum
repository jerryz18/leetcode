# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()
        ptr = head
        
        carry = False
        
        while l1 or l2 or carry != False:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            
            value = v1 + v2
            if carry == True:
                value += 1
                carry = False
            if value >= 10:
                value %= 10
                carry = True
            ptr.next = ListNode(value)
            ptr = ptr.next
            
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        
        return head.next
