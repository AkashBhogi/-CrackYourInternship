class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        d=Counter(nums)
        a=[i for i in d if d[i]==2]
        return a
        
