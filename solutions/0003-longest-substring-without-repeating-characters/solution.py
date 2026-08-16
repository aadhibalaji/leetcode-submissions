class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        

        left, right = 0, 0

        res = 0
        table = set()

        while right < len(s):

            char = s[right]

            while char in table:
                table.remove(s[left])
                left += 1
            
            table.add(char)

            res = max(res, len(table))

            right += 1

        return res




