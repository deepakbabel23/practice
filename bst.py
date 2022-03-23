class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self) -> None:
        self.root = None
    
    def insert(self, value):
        new_node = Node(value)        
        if self.root is None:
            self.root = new_node
        temp = self.root
        while(True):
            if new_node.value == temp.value:
                return False
            else:
                if new_node.value < temp.value:
                    if temp.left is None:
                        temp.left = new_node
                        return True
                    temp = temp.left
                else:
                    if temp.right is None:
                        temp.right = new_node
                        return True
                    temp = temp.right
    
    def contains(self,value):
        if self.root is None:
            return False
        temp = self.root
        while temp is not None:
            if value < temp.value:
                temp = temp.left
            elif value > temp.value:
                temp = temp.right
            elif value == temp.value:
                return True
        return False #means we have reached some leaf node and still not found this node
    
    def minimum_value(self,current_node):
        while current_node.left is not None:
            current_node = current_node.left
        return current_node.value
    
    def maximum_value(self, current_node):
        while current_node.right is not None:
            current_node = current_node.right
        return current_node.value
    
    def print_bst(self):
        """To print bst perform DFS on left subchild, then print node's value then perform
        DFS on right subchild """
        if self.root is None:
            print("empty BST")
            return
        temp = self.root
        node = temp
        left_prev = temp
        right_prev = temp
        while True:
            node = temp
            left_prev = temp.left
            right_prev = temp.right        
        
if __name__=="__main__":
    bst = BinarySearchTree()
    # 
    bst.insert(5)
    bst.insert(3)
    bst.insert(7)
    bst.insert(4)    
    bst.insert(2)
    bst.insert(6)
    bst.insert(8)
    print(bst.root)
    print(bst.contains(8))
    print(bst.contains(18))
    print(bst.minimum_value(bst.root))
    print(bst.maximum_value(bst.root))