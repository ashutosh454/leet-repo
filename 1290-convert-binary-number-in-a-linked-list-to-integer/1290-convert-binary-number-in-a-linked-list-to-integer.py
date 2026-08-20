# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        curr= head
        decimal_val = 0

        if head is None:
            return 0
        
        while curr:
            decimal_val = decimal_val*2+curr.val
            curr= curr.next
        return decimal_val