class Solution:
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 2:
            return 1
        elif n ==3:
            return 2
        else:
            d1= {}
            return self.max_product(n, d1)
        
    #applies when num>=4
    def max_product(self, num, d1):
        if num == 1:
            product = 1
        elif num == 2:
            product = 2
        elif num in d1:
            product = d1[num]
        else:
            products = []
            for i in range(2, num):
                products.append(self.max_product(i, d1) * self.max_product(num-i, d1))
            products.append(num)
            product = max(products)
            d1[num] = product
        return product
