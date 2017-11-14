class Solution(object):
    def convert(self, s, numRows):
        news = ""
        if(len(s) == 0):
            return news
        if(len(s) == 1):
            return s
        if(numRows == 1):
            return s
        l = len(s)
        space = (numRows-1)*2
        for i in range(0,numRows):
            for j in range(i,l,space):
                news = news + s[j]
                if(i>0 and i<numRows-1 and j+space-2*i < l):
                    news = news + s[j+space-2*i]
        return news