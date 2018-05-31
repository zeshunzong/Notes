class NumArray:

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums
        self.d1 = self.get_sums()
        

    def get_sums(self):
        d1 = {}
        if len(self.nums)==0:
            return d1
        else:
            d1[-1]= 0
            d1[0] = self.nums[0]
            for i in range(1, len(self.nums)):
                d1[i] = d1[i-1] + self.nums[i]
            return d1


    def sumRange(self, i,j):
        return self.d1[j] - self.d1[i-1]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)
