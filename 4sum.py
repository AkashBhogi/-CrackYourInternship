class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        a=set()
        for i in range(len(nums)):
            k=nums[i]
            for j in range(i+1,len(nums)):
                r=-nums[j]
                o,l=j+1,len(nums)-1
                while o<l:
                    s=nums[o]+nums[l]
                    if s-r+k==target:
                        a.add((nums[i],nums[j],nums[o],nums[l]))
                        o+=1
                        l-=1
                    elif s-r+k<target:
                        o+=1
                    else:
                        l-=1
        return a
