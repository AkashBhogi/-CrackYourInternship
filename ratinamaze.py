class Solution:
    def findPath(self, m, n):
        # code here
        a=[];v=[[False for i in range(len(m[0]))] for i in range(n)]
        #print(v)
        def lol(i,j,m,n,k,b,v):
            if i<0 or i>=n or j<0 or j>=len(m[0]) or m[i][j]==0 or v[i][j]==True :
                #print(i,j,5)
                return
            if i==n-1 and j==len(m[0])-1:
                b+=k
                a.append(b)
                b=""
                return
            b+=k
            #print(b)
            v[i][j]=True
            lol(i+1,j,m,n,'D',b,v)
            lol(i,j+1,m,n,'R',b,v)
            lol(i-1,j,m,n,'U',b,v)
            lol(i,j-1,m,n,'L',b,v)
            v[i][j]=False
        lol(0,0,m,n,'','',v)
        return a
            
