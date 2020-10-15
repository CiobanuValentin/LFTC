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

    '''
    def insertMain(self, val):
        id = self.search(val)
        if id != -1:
            return id
        return self.insert(val)
    '''

    def add(self, val):
        if self.__root is None:
            self.__count = 1
            self.__root = Node(val, self.__count)
            return self.__count
        return self.__insert(self.__root, val).uniqueIdentifier

    def __insert(self, root, val):
        if root is None:
            self.__count += 1
            return Node(val, self.__count - 1)
        else:
            if root.val == val:
                return root
            elif root.val < val:
                node = self.__insert(root.right, val)
                root.right = node
                return node
            else:
                node = self.__insert(root.left, val)
                root.left = node
                return node

    def search(self, val):
        return self.__search(self.__root, val)

    def __search(self, root, val):
        if root is None:  # or root.val == val:
            return -1
        if root.val == val:
            return root.uniqueIdentifier
        if root.val < val:
            return self.__search(root.right, val)
        return self.__search(root.left, val)
