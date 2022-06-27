class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        b=[0]
        if len(nums)==2:
            if nums[0]>nums[1]:
                return 0
            else:
                return 1
        def lol(a,l,r):
            if l==r:
                b[0]=l
                return
            m=(l+r)//2
            if a[m]>a[m-1] and a[m]>a[m+1]:
                b[0]=m
            elif a[m+1]>a[m]:
                lol(a,m+1,r)
            else:
                lol(a,l,m-1)
        lol(nums,0,len(nums)-1)
        
        return b[0]
        
