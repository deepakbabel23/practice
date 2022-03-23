#Doubly linked list can be used to implement a deque
class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None
        self.prev = None

class DoublyLL:
    def __init__(self,value=None) -> None:
        if value is not None:
            new_node = Node(value)
            self.head = new_node
            self.tail = new_node
            self.length = 1
        else:
            self.head = None
            self.tail = None
            self.length = 0

    def append(self,value):
        new_node = Node(value)        
        if self.head is None:
            self.head = new_node
            self.tail = self.head
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length +=1
        return True

    def pop(self):
        #empty list => return False
        #one element => make head, tail as None, set length to 0
        #more elements=> update tail, decrease length by 1
        if self.head is None:
            return False
        elif self.head == self.tail:
            del self.head
            self.head = None
            self.tail = None
            self.length = 0
            return True
        else:
            currnode = self.head
            nextnode = self.head
            while nextnode.next is not None:
                currnode = nextnode
                nextnode = nextnode.next
            self.tail = currnode
            self.tail.next = None
            del nextnode
            self.length -=1
            return True

    def pop_first(self):
        temp_node = self.head
        if self.head is None:
            return False
        elif self.head == self.tail:
            del self.head
            self.head = None
            self.tail = None
            self.length =0        
        else:
            self.head = self.head.next
            del temp_node
            self.length -=1
        return True
            
    def prepend(self,value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
        if self.tail == None:
            self.tail = new_node
        self.length +=1
        return True

    def insert(self,index,value):        
        if index > self.length:
            return False
        new_node = Node(value)
        node = self.head
 
        if index == 0:
            if self.head == self.tail == None:
                self.head = self.tail = new_node
                self.length +=1
                return True
            new_node.next = self.head
            self.head = new_node
            self.length += 1            
            return True
        if index == self.length:            
            self.tail.next = new_node
            self.tail = new_node
            self.length += 1
            return True
        if node is not None:
            for ind in range(0,self.length):
                if ind == index -1:
                    new_node.next = node.next
                    node.next = new_node
                    self.length += 1
                    return Node
                node = node.next

    def remove(self,value):
        node = self.head
        isElementFound = False
        if node is None:
            return False
        
        if(self.head.value == value):
            if(self.length == 1):            
                self.head = None
                self.tail = None
                del node
                self.length = 0                
            else:
                self.head = self.head.next
                del node
                self.length -=1
            isElementFound = True
            print(f"isElementFound: {isElementFound}")
            return True

        while node.next is not None:
            if node.next.value == value:
                if node.next == self.tail:
                    self.tail = node
                tmp = node.next
                node.next = node.next.next
                tmp.next = None
                del tmp
                self.length -=1
                isElementFound = True
                print(f"isElementFound: {isElementFound}")
                return True
            node = node.next

    def display(self):
        print("\n")
        node = self.head
        
        if node is None:
            print("linked list is empty:")
            return False

        print("linked list contents are:")
        while node is not None:
            print(node.value)
            node = node.next
        return True
    
    def get(self, index):
        retval = None
        temp = self.head
        cnt = 0
        if (index < self.length):
            while(cnt != index):                
                temp = temp.next
                cnt +=1
            print(temp.value)
            return temp
        return retval

    def reverse(self):
        if self.length == 1:
            print("DoublyLL is already reversed")
        elif self.length == 0:
            print("DoublyLL is empty")
        else:
            self.head, self.tail = self.tail, self.head
            print("the linked list has been reversed:")
            self.display()

choiceMap = {
        1: DoublyLL.insert,
        2: DoublyLL.append,
        3: DoublyLL.prepend,
        4: DoublyLL.pop,
        5: DoublyLL.pop_first,
        6: DoublyLL.remove,
        7: DoublyLL.display,
        8: DoublyLL.get,
        9: DoublyLL.reverse
        }

linked_list_obj = None
print(__name__)
if __name__=="__main__":
    #linked_list_obj = DoublyLL(5)
    linked_list_obj = DoublyLL()
    cnt = 0
    while(True):
        if cnt != 0:
            ch = input("Do you want to continue: Y/N ")
            if ch == 'N' or ch == 'n' or ch == 'no':
                print("Exiting")
                break
        print("MENU:")
        print("\n1: LL: Insert (index, value)")
        print("\n2: LL: Append (value)")
        print("\n3: LL: Prepend (value)")
        print("\n4: LL: Pop ()")
        print("\n5: LL: Pop first ()")
        print("\n6: LL: Remove (value)")
        print("\n7: LL: Display ()")
        print("\n8: LL: Get (index)")
        print("\n9: LL: Reverse ()")
        print("\n0: Exit the program")
        choice = int(input("Enter your choice from the list above: "))
        if choice == 0:
            print("Exiting this menu")
            break
        elif choice not in range(1,10):
            print("invalid choice..Try again")
        else:
            fn = choiceMap[choice]
            param = None
            try:
                params = input("Provide API params seperated by space or press Enter for no params: ")
                if params != '':
                    params = [int(param) for param in params.split()]
                    fn(linked_list_obj, *params)
                else:
                    fn(linked_list_obj)                
            except Exception as excep:
                print(excep)
                print("Try again!!")
        cnt +=1