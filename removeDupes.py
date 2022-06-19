# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        ptr = head
        while ptr:
            while ptr.next and ptr.next.val == ptr.val:
                ptr.next = ptr.next.next   
            ptr = ptr.next    
        return head
            
            
        
