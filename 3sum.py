class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        a=set()
        nums.sort()
        for i in range(len(nums)):
            t=-nums[i]
            o,l=i+1,len(nums)-1
            while o<l:
                s=nums[o]+nums[l]
                if s<t:
                    o+=1
                elif s>t:
                    l-=1
                else:
                    a.add((nums[i],nums[o],nums[l]))
                    o+=1
                    l-=1
        return a
        
