class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None
        
        # Шаг 1: Поиск узла для удаления
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            # Узел найден
            
            # Сценарий 1 и 2: у узла один ребенок или нет детей
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            
            # Сценарий 3: у узла два ребенка
            # Ищем минимальный узел в правом поддереве (самый левый)
            curr = root.right
            while curr.left:
                curr = curr.left
                
            # Заменяем значение текущего узла на найденное минимальное
            root.val = curr.val
            
            # Рекурсивно удаляем узел, чье значение мы только что скопировали
            root.right = self.deleteNode(root.right, root.val)
            
        return root