class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """

        if len(s) < len(p):
            return []

        pTable = {}

        for char in p:
            pTable[char] = pTable.get(char, 0) + 1

        
        currTable = {} 
        res = []

        for right in range(len(s)):
            currTable[s[right]] = currTable.get(s[right], 0) + 1

            left = right - len(p) + 1

            if left > 0:
                lChar = s[left - 1]

                currTable[lChar] -= 1

                if currTable[lChar] == 0:
                    del currTable[lChar]

            if left >= 0 and currTable == pTable:
                res.append(left)


        return res

    
        
