class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """


        max_ends_current = 0
        max_till_current = -9999999999999
        for i in range(len(nums)):
            max_ends_current += nums[i]

            if (max_till_current < max_ends_current):
                max_till_current = max_ends_current

            if (max_ends_current < 0):
                max_ends_current = 0
        return max_till_current
