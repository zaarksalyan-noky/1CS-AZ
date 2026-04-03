class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # Вспомогательная функция, принимающая узел и допустимые границы
        def validate(node, low=-float('inf'), high=float('inf')):
            # Пустой узел является валидным BST
            if not node:
                return True
            
            # Проверяем, находится ли значение текущего узла в допустимом диапазоне
            if node.val <= low or node.val >= high:
                return False
            
            # Рекурсивно проверяем детей
            # Для левого ребенка: верхняя граница ограничивается текущим узлом
            # Для правого ребенка: нижняя граница ограничивается текущим узлом
            return (validate(node.left, low, node.val) and 
                    validate(node.right, node.val, high))
        
        return validate(root)   