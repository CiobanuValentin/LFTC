from model.Bst import *


class SymbolTable:
    def __init__(self):
        self.bst = BST()

    def add(self, value):
        return self.bst.add(value)

    def get(self, value):
        return self.bst.search(value)

    def inorder(self):
        return self.bst.inorder()
