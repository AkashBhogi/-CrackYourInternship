# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], target: int) -> int:
        if not root:
            return 0
        d={};k=[0]
        def lol(root,s,t):
            s+=root.val
            if s==t:
                k[0]+=1
            k[0]+=d.get(s-t,0)
            d[s]=d.get(s,0)+1
            if root.left:
                lol(root.left,s,t)
            if root.right:
                lol(root.right,s,t)
            d[s]-=1
        lol(root,0,target)
        return k[0]
                
            
            
            
        
