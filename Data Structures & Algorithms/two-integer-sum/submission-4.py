class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indicies = {}
        for i, n in enumerate(nums):
            indicies[n] = i
        for i, n in enumerate(nums):
            if (target - n) in indicies and indicies[(target-n)] != i:
                return [i, indicies[(target-n)]]
        return []