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
            self.__root = Node(val, self.__count)
            self.__count = 1
            return self.__count-1
        _, addedNode = self.__insert(self.__root, val)
        return addedNode.uniqueIdentifier

    def __insert(self, root, val):
        if root is None:
            self.__count += 1
            node = Node(val, self.__count - 1)
            return node, node
        else:
            if str(root.val) == str(val):
                return root, root
            elif str(root.val) < str(val):
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
        return self.__inorder(self.__root)


    def __inorder(self, root):
        x=[]
        if root:
            x=self.__inorder(root.left)
            #print("value : "+str(root.val) + "   unique identifier:"+str(root.uniqueIdentifier))
            x.append((root.val,root.uniqueIdentifier))
            x=x+self.__inorder(root.right)
        return x
