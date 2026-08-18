# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def sameTree(self, node1, node2):
        if not node1 and not node2:
            return True
        
        if node1 and node2 and node1.val == node2.val:
            return self.sameTree(node1.left, node2.left) and self.sameTree(node1.right, node2.right)
        else:
            return False
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        if not root:
            return False

        queue = deque([root])
        while queue:
            node = queue.pop()
            if node.val == subRoot.val:
                result = self.sameTree(node, subRoot)
                if result:
                    return True
            if node.left: queue.append(node.left)
            if node.right: queue.append(node.right)

        return False

