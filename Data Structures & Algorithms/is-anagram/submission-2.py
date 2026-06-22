class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        hash_1 = {}
        hash_2 = {}

        for x in s:
            if x in hash_1:
                hash_1[x] += 1
            else:
                hash_1[x] = 1
        
        for y in t:
            if y in hash_2:
                hash_2[y] += 1
            else:
                hash_2[y] = 1

        for n in hash_1:
            if n not in hash_2 or hash_2[n] != hash_1[n]:
                return False
        return True