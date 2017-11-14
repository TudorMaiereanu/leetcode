# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        l = []
        x=0
        l1_out = 0
        l2_out = 0
        while(1):
            if(l1 == None):
                l1_out = 1
            if(l2 == None):
                l2_out = 1
                
            if(l1_out == 1 and l2_out == 1):
                if(x == 1):
                    l.append(x)
                print l
                break
            
            if(l1_out == 1):
                s = l2.val
                l2 = l2.next
            else:
                if(l2_out == 1):
                    s = l1.val
                    l1 = l1.next
                else:
                    s = l1.val + l2.val
                    l1 = l1.next
                    l2 = l2.next
            
            if(s >= 10):
                l.append(s+x-10)
                x = 1
            else:
                if(s+x >= 10):
                    l.append(s+x-10)
                    x=1
                else:
                    l.append(s+x)
                    x = 0
        return l
        