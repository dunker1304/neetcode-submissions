# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # bfs
    def goodNodes(self, root: TreeNode) -> int:
        res = 0
        q = deque([(root, float('-inf'))])
        # q = deque()
        # q.append((root,-float('inf')))

        while q:
            node, maxval = q.popleft()
            if node.val >= maxval:
                res += 1

            if node.left:
                q.append((node.left, max(maxval, node.val)))
            if node.right:
                q.append((node.right, max(maxval, node.val)))

        return res




    # dfs
    def goodNodes(self, root: TreeNode) -> int:
        res = 0

        def dfs(node, maxVal):
            nonlocal res
            if node.val >= maxVal:
                res += 1
            if node.left:
                dfs(node.left, max(maxVal, node.val))
            if node.right:
                dfs(node.right, max(maxVal, node.val))

        dfs(root, float('-inf'))
        return res