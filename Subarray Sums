class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        d = Counter({0:1})
        s=0;z=0
        for n in nums:
            s+= n 
            r=s%k 
            if r<0:
                z+=k 
            if r in d:
                z+= d[r]
            d[r] += 1
            #print(n,s,d,r,z)
        return z
