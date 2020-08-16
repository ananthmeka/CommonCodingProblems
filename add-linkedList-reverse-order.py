# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        cf = 0
        res = None
        lastNode = ListNode()
        
        while l1 or l2:
            val1 = val2 = 0
            if l1:
                val1 = l1.val
                l1 = l1.next 

            if l2:
                val2 = l2.val
                l2 = l2.next
                
            val = val1 + val2 + cf
            
            
            cf = int(val / 10)
            val = val % 10
            print(" val1[%s] val2[%s] val[%s] , cf[%s] " %(val1, val2, val, cf))
            tmp = ListNode(val)
            if res == None: # first time
                res = ListNode(tmp.val)
                lastNode = res
            else:  
                lastNode.next = tmp
                lastNode = tmp 

        if cf :
            print("in cf")
            lastNode.next = ListNode(cf,None)
        return res

l1=ListNode(9)
a=ListNode(8,l1)
l2=ListNode(1)
res = Solution().addTwoNumbers(a, l2)
while res != None:
 print(res.val)
 res = res.next
