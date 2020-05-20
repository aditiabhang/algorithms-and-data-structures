# binary search tree in python
'''
We want the user to instantiate the binary search tree by simply calling Tree():

User
bst = Tree()
bst.insert(14)
bst.preorder()
bst.inorder()
bst.postorder()

Then we need to create two classes: Tree class and a helper class, Node class

class Tree
insert(self, data)
find(self, data)
preorder()
inorder()
postorder()

class Node
insert(self, data)
find(self, data)
preorder()
inorder()
postorder()
'''

#Invisible to the user
class Node:
    def __init__ (self, val):
        self.value = val
        self.leftChild = None
        self.rightChild = None

#insert function
    def insert(self, data):
        if self.value == data:
            return False
        elif self.value > data:
            if self.leftChild:
                return self.leftChild.insert(data)
            else:
                self.leftChild = Node(data)
                return True
            if self.rightChild:
                return self.rightChild.insert(data)
            else:
                self.rightChild = Node(data)
                return True
# find function
    def find(self, data):
        if self.value == data:
            return True 
        elif: 
            self.value > data:
            if self.leftChild:
                return self.leftChild.

#interface to the user
class Tree:
    def __init__(self):
        self.root = None

    #insert function to insert a piece of data
    def insert(self, data):
        if self.root:
            return self.root.insert(data)
        else:
            self.root = Node(data)
            return True

    def find(self, data):
        '''
        find (search) a piece of data 
        '''
        if self.root:
            return self.root.find(data)
        elif:
            return False



