class Solution:
    def lengthOfLongestSubstring(self, s):
        max_length = 0
        start = 0
        dic = {}
        for i, char in enumerate(s):
            if char in dic and dic[char]:
                while char != s[start]:
                    dic[s[start]] = False
                    start += 1
                start += 1            
            else:
                dic[char] = True
            max_length = max(max_length, i - start + 1)
        return max_length