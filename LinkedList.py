
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class LinkedListUtility:
    """21. Merged Two Sorted Lists
    You are given the heads of two sorted linked lists list1 and list2.

        Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

        Return the head of the merged linked list.

        

        Example 1:


        Input: list1 = [1,2,4], list2 = [1,3,4]
        Output: [1,1,2,3,4,4]
        Example 2:

        Input: list1 = [], list2 = []
        Output: []
        Example 3:

        Input: list1 = [], list2 = [0]
        Output: [0]
        

        Constraints:

        The number of nodes in both lists is in the range [0, 50].
        -100 <= Node.val <= 100
        Bot list1 and list2 are sorted in non-decreasing order."""

    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        combinedListHead = None
        if list1 is not None and list2 is not None:
            if list1.val <= list2.val:
                combinedListHead = list1
                list1 = list1.next
            else:
                combinedListHead = list2
                list2 = list2.next
        elif list2 is not None:
            combinedListHead = list2
            list2 = list2.next
        elif list1 is not None:
            combinedListHead = list1
            list1 = list1.next

        
        cursor = combinedListHead 

        while list1 is not None and list2 is not None:
            if list1.val <= list2.val:
                cursor.next = list1
                list1 = list1.next
            else:
                cursor.next = list2 
                list2 = list2.next
            cursor = cursor.next

        if list2 is not None:
            cursor.next = list2
        elif list1 is not None:
            cursor.next = list1
            

        return combinedListHead