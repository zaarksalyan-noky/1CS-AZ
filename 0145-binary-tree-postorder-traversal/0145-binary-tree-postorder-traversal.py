class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        
        def dfs(node):
            if not node:
                return
            
            dfs(node.left)       # Шаг 1: обходим левое поддерево до конца
            dfs(node.right)      # Шаг 2: обходим правое поддерево до конца
            res.append(node.val) # Шаг 3: добавляем значение текущего узла
            
        dfs(root)
        return res