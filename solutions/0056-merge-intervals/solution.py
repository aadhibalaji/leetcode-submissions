class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """

        intervals.sort(key = lambda i : i[0])


        
        prevStart, prevEnd = intervals[0]
        res = [[prevStart, prevEnd]]
        for start, end in intervals[1:]:
            if start <= prevEnd:
                res.pop()
                res.append([prevStart, max(end, prevEnd)])
                prevStart, prevEnd = prevStart, max(end, prevEnd)
            else:
                res.append([start, end])
                prevStart, prevEnd = start, end
            
        return res
        
