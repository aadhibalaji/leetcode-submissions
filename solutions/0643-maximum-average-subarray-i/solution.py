class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """

        left, right = 0, 0
        res = float('-inf')
        total = 0

        while right < len(nums):
            
            total += nums[right]

            if (right - left + 1) > k:
                total -= nums[left]
                left += 1

            if (right - left + 1) == k:
                res = max(res, total / float(k))

            right += 1
            
        return res
        
