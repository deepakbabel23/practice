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
    
    def print_bst_bfs(self):
        """Let's do BFS here """
        current_node = self.root
        my_queue =[]
        results = []
        my_queue.append(current_node)
        while (len(my_queue) >0):
            current_node = my_queue.pop(0)
            results.append(current_node.value)
            if current_node.left is not None:
                my_queue.append(current_node.left)
            if current_node.right is not None:
                my_queue.append(current_node.right)
        print(results)

    def print_bst_dfs_pre(self):
        #print node value, then left and then right
        results = []
        def traverse(node):
            results.append(node.value)
            if node.left is not None:
                traverse(node.left)
            if node.right is not None:
                traverse(node.right)
        traverse(self.root)
        print(results)

    def print_bst_dfs_post(self):
        #print left and then right and then parent
        results = []
        def traverse(node):            
            if node.left is not None:
                traverse(node.left)
            if node.right is not None:
                traverse(node.right)
            results.append(node.value)
        traverse(self.root)
        print(results)
    
    def print_bst_dfs_inorder(self):
        #print left, parent and then right
        results = []
        def traverse(node):            
            if node.left is not None:
                traverse(node.left)
            results.append(node.value)
            if node.right is not None:
                traverse(node.right)
            
        traverse(self.root)
        print(results)
        
if __name__=="__main__":
    bst = BinarySearchTree()
    bst1 = BinarySearchTree()
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

    bst1.insert(47)
    bst1.insert(21)
    bst1.insert(76)
    bst1.insert(18)
    bst1.insert(27)
    bst1.insert(52)
    bst1.insert(82)
    bst1.insert(17)
    bst1.insert(28)
    bst1.insert(51)
    bst1.insert(83)
    bst1.print_bst_bfs()