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

        # Create a dummy node to start the new list
        dummy = ListNode()
        tail = dummy  # tail points to the last node in the merged list

        # While both lists are not empty
        while list1 and list2:
            # Pick the smaller value and attach it to the tail
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next

            # Move tail to the newly added node
            tail = tail.next

        # One of the lists might still have nodes left, attach them
        if list1:
            tail.next = list1
        else:
            tail.next = list2

        # The first node after dummy is the real head of the merged list
        return dummy.next
