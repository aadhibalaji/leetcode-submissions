class Solution(object):
    def lengthOfLongestSubstringKDistinct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """

        res = 0
        left = 0
        table = {}

        for right in range(len(s)):
            table[s[right]] = table.get(s[right], 0) + 1

            while len(table) > k:
                if table[s[left]] > 1:
                    table[s[left]] -= 1
                else:
                    del table[s[left]]
                left += 1

            res = max(res, right - left + 1)


        return res


        
        
