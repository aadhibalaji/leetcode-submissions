class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        

        res = 0
        left = 0
        table = {}
        maxFreq = 0

        for right in range(len(s)):
            table[s[right]] = table.get(s[right], 0) + 1

            maxFreq = max(maxFreq, table[s[right]])

            while (right - left + 1) - maxFreq > k:
                table[s[left]] -= 1

                left += 1

            res = max(res, right - left + 1)

        return res
