class Solution:
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        arr = [False] * (num+1)
        arr[0] = 0
        if num==0:
            return arr
        arr[1] = 1
        if num<=1:
            return arr
        for i in range(2, num+1):
            ones = i % 2 + arr[i//2]
            arr[i] = ones
        return arr
