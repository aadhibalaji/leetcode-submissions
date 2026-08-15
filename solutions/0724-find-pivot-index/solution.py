class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """


        
        prefix = [0] * (len(nums) + 1)

        for i, n in enumerate(nums):
            prefix[i + 1] = prefix[i] + n


        end = len(prefix) - 1
        pivot = -1
        for i in range(1, len(prefix)):

            left = prefix[i - 1]
            right = prefix[end] - prefix[i]

            if left == right:
                #subtract 1 because we added an extra index in the prefix sum array
                return i - 1
        

        return pivot
        
        

        
