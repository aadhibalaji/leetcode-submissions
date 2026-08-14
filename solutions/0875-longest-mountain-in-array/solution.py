class Solution(object):
    def longestMountain(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        
        i = res = 0

        while i < len(arr):
            
            base = i

            #walk up 
            while i < len(arr) - 1 and arr[i] < arr[i + 1]:
                i += 1


            if i == base:
                i += 1
                continue
            peak = i

            #walk down
            while i + 1 < len(arr) and arr[i] > arr[i + 1]:
                i += 1
            
            if i == peak:
                i += 1 
                continue

            res = max(res, i - base + 1)
        
        return res


