class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """

        if head.next is None:
            head = head.next
            return head

        curr_pointer = prev_pointer = head
        i = 1

        while curr_pointer.next is not None:
            curr_pointer = curr_pointer.next

            if i > n:
                prev_pointer = prev_pointer.next

            i += 1

        if i == n:
            head = head.next
            return head

        temp = prev_pointer.next
        prev_pointer.next = temp.next

        return head
