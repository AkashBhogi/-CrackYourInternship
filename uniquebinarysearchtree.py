class Solution:
    def numTrees(self, n: int) -> int:
        d=[0 for _ in range(n + 1)]
        d[0] = 1;d[1] = 1
        for i in range(2, n + 1):
            for j in range(1, n + 1):
                d[i]+=d[j - 1]*d[i - j]

        return d[-1]
