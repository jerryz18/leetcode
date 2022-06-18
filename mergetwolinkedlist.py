# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()
        ptr = ListNode()
        head.next = ptr
        
        if list1 == None and list2 == None:
            return None
        elif list1 == None:
            return list2
        elif list2 == None:
            return list1
        
        while list1 and list2:
            if list1.val < list2.val:
                ptr.next = list1
                ptr = ptr.next
                list1 = list1.next
            else:
                ptr.next = list2
                ptr = ptr.next
                list2 = list2.next
        if list1 or list2:
            ptr.next = list1 if list1 else list2
            
        return head.next.next
