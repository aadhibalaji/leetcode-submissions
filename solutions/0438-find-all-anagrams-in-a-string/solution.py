class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        
        pTable = {}

        for i in range(len(p)):
            pTable[p[i]] = pTable.get(p[i], 0) + 1

        
        table = {}
        res = []
        left = 0

        for right in range(len(s)):
            table[s[right]] = table.get(s[right], 0) + 1

            if right - left + 1 > len(p):
                if table[s[left]] > 1:
                    table[s[left]] -= 1
                else:
                    del table[s[left]]
                left += 1

            if table == pTable: 
                res.append(left)

        return res
