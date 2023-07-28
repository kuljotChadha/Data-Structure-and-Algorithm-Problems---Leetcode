# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        arr=[]
        Flag=True

        def dfs(root):
            nonlocal Flag
            if not root:
                return
            dfs(root.left)

            if arr and root.val <= arr[-1]:
                Flag=False
            
            arr.append(root.val)

            dfs(root.right)

        dfs(root)
        print(arr)
        return Flag



        