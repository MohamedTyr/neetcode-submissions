import math 

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
       full_product = math.prod(nums)
       nonzero_prod = 1
       zero_cnt = 0
       for i in nums:
            if i != 0:
                nonzero_prod = nonzero_prod * i
            else:
                zero_cnt += 1

       final = [0] * len(nums)
       if zero_cnt > 1:
            return [0] * len(nums)
       if zero_cnt == 1 or zero_cnt == 0: 
            for i in range(len(nums)):
                if nums[i] != 0:
                    final[i] = full_product // nums[i]
                else:
                    final[i] = nonzero_prod
            return final