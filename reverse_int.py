class Solution(object):
    def reverse(self, x):
        if(x>2147483641):
            return 0
        if(x<0):
            y = -1 * x
            print y
            if(y>=2147483648):
                return 0
        newx = 0
        if(x < 0):
            y = -1 * x
            while(y!=0):
                newx = newx * 10 + (y % 10)
                y = y / 10
            return -newx
        else:
            while(x!=0):
                newx = newx * 10 + (x % 10)
                x = x / 10
            return newx    
        