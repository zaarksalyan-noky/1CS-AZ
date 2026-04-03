class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        
        def dfs(node):
            if not node:
                return
            
            dfs(node.left)       # Шаг 1: рекурсивно обходим левое поддерево
            res.append(node.val) # Шаг 2: посещаем текущий узел (добавляем значение в список)
            dfs(node.right)      # Шаг 3: рекурсивно обходим правое поддерево
            
        dfs(root)
        return res      