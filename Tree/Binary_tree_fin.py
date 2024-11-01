class Node:
    def __init__(self, value):
        self.value = value
        self.LeftChild = None
        self.RightChild = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def Insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            current = self.root
            while True:
                if value < current.value:
                    if current.LeftChild is None:
                        current.LeftChild = Node(value)
                        break
                    current = current.LeftChild
                else:
                    if current.RightChild is None:
                        current.RightChild = Node(value)
                        break
                    current = current.RightChild

    def Find(self, value):
        current = self.root
        while current is not None:
            if value < current.value:
                current = current.LeftChild
            elif value > current.value:
                current = current.RightChild
            else:
                return True
        return False

    def PreOrder(self, root):
        if root is None:
            return
        print(root.value, end=" ")
        self.PreOrder(root.LeftChild)
        self.PreOrder(root.RightChild)

    def Inorder(self, root):
        if root is None:
            return
        self.Inorder(root.LeftChild)
        print(root.value, end=" ")
        self.Inorder(root.RightChild)

    def PostOrder(self, root):
        if root is None:
            return
        self.PostOrder(root.LeftChild)
        self.PostOrder(root.RightChild)
        print(root.value, end=" ")

    def Remove(self, root, value):
        if root is None:
            return None

        if value < root.value:
            root.LeftChild = self.Remove(root.LeftChild, value)
        elif value > root.value:
            root.RightChild = self.Remove(root.RightChild, value)
        else:
            if root.LeftChild is None:
                temp = root.RightChild
                del root
                return temp
            elif root.RightChild is None:
                temp = root.LeftChild
                del root
                return temp
            else:
                succParent = root
                succ = root.RightChild

                while succ.LeftChild is not None:
                    succParent = succ
                    succ = succ.LeftChild

                if succParent != root:
                    succParent.LeftChild = succ.RightChild
                else:
                    succParent.RightChild = succ.RightChild

                root.value = succ.value

                del succ
                return root

        return root

    def display(self):
        if self.root is not None:
            self._display_recursive(self.root, 0, "Root: ")

    def _display_recursive(self, node, level, prefix):
        if node is not None:
            print(" " * (level * 4) + prefix + str(node.value))
            if node.LeftChild is not None or node.RightChild is not None:
                self._display_recursive(node.LeftChild, level + 1, "L--- ")
                self._display_recursive(node.RightChild, level + 1, "R--- ")




