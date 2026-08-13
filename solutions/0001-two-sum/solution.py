class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        table = {}
        res = []
        for i in range(len(nums)):
            difference = target - nums[i]

            if difference in table:
                return [table[difference], i]
        
            
            table[nums[i]] = i

        return []

            
        
