# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        i = list1
        j = list2

        dummy = ListNode(0)
        current = dummy

        while i and j:
            if i.val < j.val:
                current.next = i
                i = i.next
            else:
                current.next = j
                j = j.next
            
            current = current.next

        if i:
            current.next = i
        else:
            current.next = j
        
        return dummy.next
        