class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        map = {}
        n = len(nums)

        for i in range(len(nums)):
            map[nums[i]] = map.get(nums[i], 0) + 1
        
        for key in map:
            if (map[key] > (n // 2)):
                return key
        

