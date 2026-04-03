class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        # Базовый случай: нашли свободное место, создаем узел
        if not root:
            return TreeNode(val)

        # Выбираем направление поиска в зависимости от значения
        if val < root.val:
            # Значение меньше: рекурсивно идем в левое поддерево
            root.left = self.insertIntoBST(root.left, val)
        else:
            # Значение больше: рекурсивно идем в правое поддерево
            root.right = self.insertIntoBST(root.right, val)

        # Возвращаем корень (изменения "прикрепятся" на возврате из рекурсии)
        return root