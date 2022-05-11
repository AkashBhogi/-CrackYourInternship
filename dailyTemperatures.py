class Solution:
    def dailyTemperatures(self, temp: List[int]) -> List[int]:
        stack = []
        ans = [0]*len(temp)
        i = 0
        
        while i<len(temp):
            if stack and stack[-1][0]<temp[i]:
                val,idx = stack.pop()
                ans[idx] = i-idx 
                
            else:
                stack.append((temp[i],i))
                i+=1
        
        return ans
