class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        

        intervals.sort(key = lambda i : i[0])

        heap = []

        heapq.heappush(heap, intervals[0][1])
        
        
        for start, end in intervals[1:]:

            if heap[0] <= start:
                heapq.heappop(heap)
                heapq.heappush(heap, end)
                continue

            heapq.heappush(heap, end)

        return len(heap)

