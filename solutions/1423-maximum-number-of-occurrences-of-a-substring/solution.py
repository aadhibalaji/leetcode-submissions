class Solution(object):
    def maxFreq(self, s, maxLetters, minSize, maxSize):
        """
        :type s: str
        :type maxLetters: int
        :type minSize: int
        :type maxSize: int
        :rtype: int
        """
        
        table = {}
        res = 0

        for i in range(len(s) - minSize + 1):
            subString = s[i:i+ minSize]
            if len(set(subString)) <= maxLetters:
                table[subString] = table.get(subString, 0) + 1
                res = max(res, table[subString])

        return res
