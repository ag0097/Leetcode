# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = [(root,0)]
        dic = {}
        ans = []
        while(queue):
            k = queue
            queue = []
            for v,i in k:
                
                if i in dic:
                    dic[i].append(v.val)
                
                else:
                    dic[i] = [v.val]
                    
                if v.left:
                    queue.append((v.left,i-1))
                
                if v.right:
                    queue.append((v.right,i+1))
            
            queue.sort(key = lambda x:(x[1],x[0].val))
                
        for i in sorted(dic):
            ans.append(dic[i])
            
        return ans