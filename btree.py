class Node:
    def __init__(self,value, name="") -> None:
        self.value = value
        self.left = None
        self.right = None
        self.to_traverse = False
        self.name = name

class BinaryTree:
    def __init__(self) -> None:
        self.root = None
    def insert(self):
        """
                A(4)
            B(5)        C(4)
        D(6)         E(4)    F(7)
                   G(4)
                      H(4)

        """
        new_node = Node(4,'A')
        new_node1 = Node(5,'B')
        new_node2 = Node(4,'C')
        new_node3 = Node(6,'D')
        new_node4 = Node(4,'E')
        new_node5 = Node(7,'F')
        new_node6 = Node(4,'G')
        new_node7 = Node(4,'H')

        self.root = new_node
        new_node.left = new_node1
        new_node.right = new_node2
        new_node1.left = new_node3
        new_node2.left = new_node4
        new_node2.right = new_node5
        new_node4.left = new_node6
        new_node6.right = new_node7

    def print_bt_bfs(self):
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

    def traverse_longest_same_val_path(self, current_node):
        path = []
        path_nodes = []
        current_node.to_traverse = True
        def traverse_node(current_node):
            path.append(current_node.value)
            path_nodes.append(current_node)
            if current_node.left is None and current_node.right is None:
                return
            if current_node.left is not None:
                if current_node.value == current_node.left.value:
                    current_node.left.to_traverse = True                    
                    traverse_node(current_node.left)
            if current_node.right is not None:
                if current_node.value == current_node.right.value:
                    current_node.right.to_traverse = True
                    traverse_node(current_node.right)
        traverse_node(current_node)
        print(path)
        for node in path_nodes:
            print("to_traverse for this node with name {} is = {}".format(node.name, node.to_traverse))

if __name__=="__main__":
    bt = BinaryTree()
    bt.insert()
    bt.print_bt_bfs()
    bt.traverse_longest_same_val_path(bt.root)