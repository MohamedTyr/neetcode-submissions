class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
       map = defaultdict(int)
       for i in nums: 
            map[i]+=1
       array = [[] for _ in range(len(nums) + 1)]
       for number, count in map.items():
            array[count].append(number)
       res = [] 
       for i in reversed(array):
            for number in i:
                res.append(number)
            if len(res)==k:
                return res