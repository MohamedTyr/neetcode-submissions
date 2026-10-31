import math 

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
       prod = 1
       zero_cnt = 0
       for i in nums:
            if i != 0:
                prod = prod * i
            else:
                zero_cnt += 1

       final = [0] * len(nums)
       if zero_cnt > 1:
            return final
       for i in range(len(nums)):
            if zero_cnt:
                final[i] = 0 if nums[i] else prod
            else:
                final[i] = prod // nums[i]
       return final