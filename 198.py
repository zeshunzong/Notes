class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d1 = {}
        return self.rob_dp(nums, len(nums)-1, d1)
        
    def rob_dp(self, arr, i, dictionary):
        if i<0:
            return 0
        if i==0:
            money = arr[0]
        elif i==1:
            money = max(arr[0:2])
        elif i in dictionary:
            money = dictionary[i]
        else:
            money = max([self.rob_dp(arr, i-2, dictionary)+arr[i], self.rob_dp(arr, i-1, dictionary)])
            dictionary[i] = money
        return money
        
        
