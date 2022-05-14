# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        k=head;f=head;m=0
        while head!=None:
            m+=1
            head=head.next
        for i in range(1,m-n):
            k=k.next
        if m==n:
            return f.next
        else:
            k.next=k.next.next
            return f
