class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        
        points.sort(key = lambda i:i[1])
        res = 1
        arrowPos = points[0][1]

        for start, end in points[1:]:

            if start > arrowPos:
                res += 1
                arrowPos = end
        
        return res
