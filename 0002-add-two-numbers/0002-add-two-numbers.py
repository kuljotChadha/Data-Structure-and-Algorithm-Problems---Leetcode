# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        def findvalue(head):
            count=0
            cur=head
            total=0

            while cur:
                total+=cur.val*(10**count)
                count+=1
                cur=cur.next

            return total

        totalL1 = findvalue(l1)
        totalL2 = findvalue(l2)

        totall1l2 = totalL1 + totalL2
        
        final=ListNode(val=-1)
        ans=final 

        if totall1l2 == 0:
            final.next=ListNode(val=totall1l2)
             
        while totall1l2:
            value= totall1l2 % 10
            final.next=ListNode(val=value)
            final=final.next
            totall1l2 = totall1l2//10
            
        return ans.next
