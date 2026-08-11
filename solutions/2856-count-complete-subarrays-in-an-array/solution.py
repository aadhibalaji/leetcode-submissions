class Solution(object):
    def countCompleteSubarrays(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        res = 0
        table = {}
        n = len(nums)
        right = 0
        distinct = len(set(nums))

        for left in range(n):
            if left > 0:
                remove = nums[left - 1]
                table[remove] -= 1
                if table[remove] == 0:
                    table.pop(remove)

            while right < n and len(table) < distinct:
                table[nums[right]] = table.get(nums[right], 0) + 1
                right += 1
            if len(table) == distinct:
                res += n - right + 1
        
        return res
        
