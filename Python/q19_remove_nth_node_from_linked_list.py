# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """

        if head==None: return None

        dummy = ListNode(None)
        dummy.next = head
        begin = tail = dummy
        counter = 0
        while tail:
            if counter<=n:
                tail=tail.next
                counter+=1
            else:
                tail=tail.next
                begin=begin.next
        if begin==dummy: return head.next
        else:
            begin.next=begin.next.next
        return head

        
