# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        if root.left==root.right==None: return 1
        global count
        count=0
        self.traversal(root)
        if root.val == 0: count+=1
        return count

    def traversal(self,root):
        global count
        if root == None: return 1
        left = self.traversal(root.left)
        right = self.traversal(root.right)
        if left==0 or right==0:
            root.val=2
            count+=1
            return 2
        elif left==2 or right==2:
            root.val=1
            return 1            
        else: return 0
        