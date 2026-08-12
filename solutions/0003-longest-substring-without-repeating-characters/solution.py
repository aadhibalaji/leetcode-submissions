class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        table = set()

        left = 0

        res = 0

        for right in range(len(s)):
            
            if len(table) > res:
                res = len(table)
            
            while s[right] in table:
                table.remove(s[left])
                left += 1
            
            table.add(s[right])

        if len(table) > res:
            res = len(table)

        return res



                

