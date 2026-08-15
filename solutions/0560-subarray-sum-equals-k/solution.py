class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        count = 0

        running_sum = 0
        seen = {0:1}

        for n in nums:
            running_sum += n

            count += seen.get(running_sum - k, 0)

            seen[running_sum] = seen.get(running_sum, 0) + 1

        
        return count
        
        
        

