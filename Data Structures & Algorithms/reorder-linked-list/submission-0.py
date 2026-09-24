# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head

        # Find end of first half
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        # Split
        current = slow.next
        slow.next = None

        # Reverse second half
        prev = None
        while current:
            nextt = current.next
            current.next = prev
            prev = current
            current = nextt

        # Merge
        left = head
        right = prev

        while right:
            left_next = left.next
            right_next = right.next

            left.next = right
            right.next = left_next

            left = left_next
            right = right_next