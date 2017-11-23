def palcheck(s):
        s_list_rev = s[::-1]
        if(s == s_list_rev):
            return 1
        else:
            return 0
                      
class Solution(object):
    def longestPalindrome(self, s):
        max_len = 0
        lis = list(s)
        l_sub = ""
        for i in xrange(len(s)):
            for j in xrange(i,len(s)):
                if(palcheck(lis[i:j+1])):
                    sub = lis[i:j+1]
                    if(len(sub) >= max_len):
                        max_len = len(sub)
                        l_sub = sub
        s = ''.join(l_sub)
        return s