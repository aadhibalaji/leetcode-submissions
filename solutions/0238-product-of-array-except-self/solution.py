class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        #build left and right product arrays

        
        left = [1] * (len(nums) + 1)
        right = [1] * (len(nums) + 1)

        #left 
        for i, n in enumerate(nums):
            left[i + 1] = left[i] * n

        #right
        for i in range(len(nums) - 1, -1, -1):
            right[i] = right[i + 1] * nums[i]

        res = []

        for i in range(len(nums)):
            res.append(left[i] * right[i + 1])


        return res

