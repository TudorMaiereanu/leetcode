# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        link1 = head
        c1 = 0
        
        while(link1 != None):
            link1 = link1.next
            c1 = c1 + 1
        
        res = []
        if(c1 == 1 and n == 1):
            return res
        
        if(c1<n):
            None.next
        
        c2 = 0
        
        while(head != None):
            print(head.val)
            
            if( c2 == c1 - n):
                if(head.next == None):
                    break
                else:
                    head = head.next
                
            res.append(head.val)
            head = head.next
            
            c2 = c2 + 1
            
        return res
            
        
        
        
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """