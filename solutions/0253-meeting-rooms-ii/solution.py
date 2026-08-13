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
            if start < heap[0]:
                heapq.heappush(heap, end)
            else:
                heapq.heappop(heap)
                heapq.heappush(heap, end)

        print(heap)
        return len(heap)
