class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        
        def dfs(node):
            if not node:
                return
            
            res.append(node.val) # Шаг 1: сначала посещаем текущий узел
            dfs(node.left)       # Шаг 2: затем рекурсивно обходим левое поддерево
            dfs(node.right)      # Шаг 3: затем рекурсивно обходим правое поддерево
            
        dfs(root)
        return res