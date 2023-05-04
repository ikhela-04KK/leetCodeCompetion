# from functools import reduce 

import math


class solution(object):

    def arraySignAndProd(self,nums):
        c_neg, zeros = 0, 0
        for i in nums:
            c_neg += (i < 0)
            zeros += (i == 0)
        return 0 if zeros else (-1 if c_neg % 2 else 1)



nums = solution()
print(nums.arraySignAndProd([1,2,10]))