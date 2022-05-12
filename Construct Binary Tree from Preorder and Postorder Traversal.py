# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructFromPrePost(self, pre: List[int], post: List[int]) -> Optional[TreeNode]:
        def lol(pre,post,root,g):
            if g[0]>=len(pre):
                return
            try:
                if pre[g[0]] in post[:post.index(root.val)]:
                    root.left=TreeNode(pre[g[0]])
                    g[0]+=1
                else:
                    return
                lol(pre,post,root.left,g)
            except:
                return
            try:
                if pre[g[0]] in post[:post.index(root.val)]:
                    root.right=TreeNode(pre[g[0]])
                    g[0]+=1
                else:
                    return
                lol(pre,post,root.right,g)
            except:
                return
        root=TreeNode(pre[0])
        k=root
        lol(pre,post,root,[1])
        return k
