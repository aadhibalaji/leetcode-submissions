class Solution(object):
    def lengthOfLongestSubstring(self, s):


        left = 0 
        res = 0
        table = {}

        for right in range(len(s)):
            if s[right] in table and table[s[right]] >= left:
                left = table[s[right]] + 1
            
            table[s[right]] = right
            res = max(res, right - left + 1)

        return res
