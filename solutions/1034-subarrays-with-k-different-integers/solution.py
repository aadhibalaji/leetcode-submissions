class Solution(object):
    def subarraysWithKDistinct(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        def atMost(k):
            if k == 0:
                return 0 

            res = 0
            table = {}
            left = 0

            for right in range(len(nums)):
                table[nums[right]] = table.get(nums[right], 0) + 1

                while len(table) > k:
                
                    if table[nums[left]] > 1:
                        table[nums[left]] -= 1
                    else:
                        del table[nums[left]]
                
                    left += 1

                res += right - left + 1
            
            return res


            

        return atMost(k) - atMost(k - 1)
        
