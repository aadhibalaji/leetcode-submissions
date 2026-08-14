class Solution(object):
    def averageValue(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        divisible = 0
        count = 0
        for num in nums:
            if num % 6 == 0:
                divisible += num
                count += 1
        
        if divisible != 0:
            return divisible / count
        
        return 0
        
