class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        k %= len(nums)
        
        newStart = len(nums) - k

        res = []

        for i in range(newStart, len(nums)):
            
            res.append(nums[i])

        
        for i in range(0, newStart):
            res.append(nums[i])
            
        for i in range(len(nums)):
            nums[i] = res[i]
       

