# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        a=None;b=None;p=-1;s=-1
        while l1 is not None:
            k=l1
            l1=l1.next
            k.next=a
            a=k
            p+=1
        while l2 is not None:
            k=l2
            l2=l2.next
            k.next=b
            b=k
            s+=1
        #print(a,b)
        k=0;r=0;h=0
        while a is not None:
            r=r+(a.val)*pow(10,p)
            a=a.next
            p-=1
        k=0
        while b is not None:
            h=h+(b.val)*pow(10,s)
            b=b.next
            s-=1
        #print(r,h)
        r=r+h
        #print(r)
        r=str(r);r=reversed(r);e=ListNode(0);g=e
        for i in r:
            g.next=ListNode(int(i))
            g=g.next
        return e.next
            
            
            
