class Solution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        res = 0

        running_sum = 0
        seen = {0: -1}

        for i, n in enumerate(nums):
            if n == 0:
                running_sum += -1
            else:
                running_sum += 1

            if running_sum in seen:
                res = max(res, i - seen[running_sum])
                continue

            seen[running_sum] = i
        
        return res
        
        
