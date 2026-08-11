class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """


        #sort by starting value of each interval
        intervals.sort(key = lambda i : i[0])
        res = 0
        tracker = [intervals[0]]

        for start, end in intervals[1:]:
            lastEnd = tracker[-1][1]

            if start < lastEnd:
                res += 1
                if end < lastEnd:
                    tracker[-1] = [start, end]
                continue
                    
            tracker.append([start, end])

        return res
        
