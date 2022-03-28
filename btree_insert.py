import datetime
from email.policy import default
from time import sleep
import random

def toss_coin_random():
    x = random.randint(0,1)
    return x

def toss_coin():
    sleep(.1)
    x = int(datetime.datetime.now().strftime("%Y%m%d%H%M%S"))
    return x

class Node():
    def __init__(self, value) -> None:
        self.left = None
        self.right = None
        self.value = value

class BinaryTree():
    def __init__(self) -> None:
        self.root = None
    
    def insert(self,value):
        node = Node(value)
        if self.root is None:            
            self.root = node
            return
        else:
            tempnode = self.root            
            if toss_coin_random() == 0:
                while tempnode.left is not None:
                    print("Traverse further left".format(value))
                    tempnode = tempnode.left
                if tempnode.left is None:                        
                    print("Inserting {} into left".format(value))
                    tempnode.left = node
                    return
            else:
                while tempnode.right is not None:
                    print("Traverse further right".format(value))
                    tempnode = tempnode.right
                if tempnode.right is None:                        
                    print("Inserting {} into right".format(value))
                    tempnode.right = node
                    return

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

    def print_bt_dfs(self):
        """Pre -order"""
        if self.root is None:
            return None
        temp = self.root
        def print_dfs(tmp):            
            print(tmp.value)
            if tmp.left is not None:
                print_dfs(tmp.left)
            if tmp.right is not None:
                print_dfs(tmp.right)
        print_dfs(temp)

    def pretty_display(self):
        """pretty display is like file explorer view"""
        if self.root is None:
            print(self.root.value)
            return
        temp = self.root
        num_spaces = 2
        mydict = dict()
        def pp_display(tmp, num_spaces):
            print(tmp)
            mydict[tmp.value] = num_spaces
            if tmp.left is not None:                
                pp_display(tmp.left, mydict[tmp.value] +2)
            if tmp.right is not None:                
                pp_display(tmp.right, mydict[tmp.value] +2)
        pp_display(temp, num_spaces)
        for k,v in mydict.items():
            for i in range(v):
                print(" ",end=" ")
            print(k)

def generate_random_tree( size=5):
    btree = BinaryTree()
    for i in range(size):
        val = 10*(i+1)
        print(val)
        btree.insert(val)
    return btree

if __name__=="__main__":    
    #btree = generate_random_tree(5)
    #btree.print_bt_bfs()
    btree1 = BinaryTree()    
    btree1.insert(1)
    btree1.insert(2)
    btree1.insert(3)
    btree1.insert(4)
    btree1.insert(5)
    btree1.print_bt_dfs()
    btree1.pretty_display()