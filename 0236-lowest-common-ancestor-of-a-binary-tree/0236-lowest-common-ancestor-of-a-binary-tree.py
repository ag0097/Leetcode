# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        one_found = False
        two_found = False
        stack = [(root, False, 1)]
        while stack:
            node, visited, h = stack.pop()
            if node:
                if visited:
                    if node == p or node == q:
                        if one_found:
                            two_found = True
                        else:
                            one_found = True
                            h_found = h
                        
                    if two_found and h < h_found:
                        return node
                    
                    if one_found:
                        h_found = min(h_found, h)
                    
                else:
                    stack.append((node, True, h))
                    stack.append((node.right, False, h + 1))
                    stack.append((node.left, False, h + 1))