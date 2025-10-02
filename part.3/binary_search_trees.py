class BSTreeNode:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None

    def __repr__(self):
        return f'({self.left}) <--({self.value})--> ({self.right})'


class BSTree:
    def __init__(self, value=None):
        self.root = BSTreeNode(value)
        self.elements = 0

    def set(self, value):
        node = self.root
        while True:
            if value >= node.value:
                if node.right is None:
                    node.right = BSTreeNode(value)
                    break
                else:
                    node = node.right
            elif value < node.value:
                if node.left is None:
                    node.left = BSTreeNode(value)
                    break
                else:
                    node = node.left

    def get(self, value):
        node = self.root
        while node:
            if value == node.value:
                return node
            elif value > node.value:
                node = node.right
            else:
                node = node.left
        return None


bst = BSTree(10)
bst.set(14)
bst.set(11)
bst.set(13)
bst.set(9)
print(bst.root)
print('-' * 50)
print(bst.get(13))
print('-' * 50)
print(bst.get(21))
