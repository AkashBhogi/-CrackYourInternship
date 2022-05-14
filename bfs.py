#User function Template for python3

class Solution:
    
    #Function to return Breadth First Traversal of given graph.
    def bfsOfGraph(self, V, adj):
        r=V
        v=[0]*r
        v[0]=1
        a=[0];b=[]
        #a.append(0)
        while a:
            k=a.pop(0)
            #print(a)
            b.append(k)
            for i in adj[k]:
                if v[i]==0:
                    a.append(i)
                    v[i]=1
        #print(b)
        return b
        # code here
        

#{ 
#  Driver Code Starts
if __name__ == '__main__':
    T=int(input())
    for i in range(T):
        V, E = map(int, input().split())
        adj = [[] for i in range(V)]
        for _ in range(E):
            u, v = map(int, input().split())
            adj[u].append(v)
        ob = Solution()
        ans = ob.bfsOfGraph(V, adj)
        for i in range(len(ans)):
            print(ans[i], end = " ")
        print()
        

# } Driver Code Ends
