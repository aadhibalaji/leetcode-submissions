class Solution(object):
    def subarraysDivByK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        count = 0
        running_sum = 0
        seen = {0: 1}

        for i, n in enumerate(nums):
            running_sum += n

            remainder = running_sum % k

        
            count += seen.get(remainder, 0)

            seen[remainder] = seen.get(remainder, 0) + 1

        
        return count

        
