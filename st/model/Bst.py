class Node:
    def __init__(self, val, uniqI):
        self.left = None
        self.right = None
        self.val = val
        self.uniqueIdentifier = uniqI


class BST:
    def __init__(self):
        self.__root = None
        self.__count = 0

    def add(self, val):
        if self.__root is None:
            self.__count = 1
            self.__root = Node(val, self.__count)
            return self.__count
        _, addedNode = self.__insert(self.__root, val)
        return addedNode.uniqueIdentifier

    def __insert(self, root, val):
        if root is None:
            self.__count += 1
            node = Node(val, self.__count - 1)
            return node, node
        else:
            if root.val == val:
                return root, root
            elif root.val < val:
                node, addedNode = self.__insert(root.right, val)
                root.right = node
                return root, addedNode
            else:
                node, addedNode = self.__insert(root.left, val)
                root.left = node
                return root, addedNode

    def search(self, val):
        return self.__search(self.__root, val)

    def __search(self, root, val):
        if root is None:
            return -1
        if root.val == val:
            return root.uniqueIdentifier
        if root.val < val:
            return self.__search(root.right, val)
        return self.__search(root.left, val)

    def inorder(self):
        self.__inorder(self.__root)

    def __inorder(self, root):
        if root:
            self.__inorder(root.left)
            print(root.val)
            self.__inorder(root.right)
