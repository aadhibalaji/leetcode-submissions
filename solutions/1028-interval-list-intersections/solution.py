class Solution(object):
    def intervalIntersection(self, firstList, secondList):
        """
        :type firstList: List[List[int]]
        :type secondList: List[List[int]]
        :rtype: List[List[int]]
        """
        
        if not firstList or not secondList:
            return []


        res = []
        i = 0
        j = 0

        while i < len(firstList) and j < len(secondList):
            
            a, b = firstList[i]
            c, d = secondList[j]

            if max(a, c) <= min(b, d):
                res.append([max(a, c), min(b, d)])

            if b < d:
                i += 1
            elif d < b:
                j += 1
            else:
                i += 1
                j += 1
            
        
        return res
            
        
            
        
