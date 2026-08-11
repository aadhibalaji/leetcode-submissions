class Solution(object):
    def numberOfSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
        def odd(k):

            left = 0
            table = {}
            res = 0

            oddCounter = 0


            for right in range(len(nums)):
                if nums[right] % 2 != 0:
                    oddCounter += 1

                #window is invalid if there are more than k odd numbers
                while oddCounter > k:
                    if nums[left] % 2 != 0:
                        oddCounter -= 1
                    
                    left += 1

                res += right - left + 1

            return res

        return odd(k) - odd(k - 1)
