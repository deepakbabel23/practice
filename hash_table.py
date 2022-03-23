import enum


class HashTable:
    def __init__(self, size=7) -> None:
        self.data_map = [None] * size
        print(self.data_map)
    
    def __hash(self,key):
        my_hash = 0
        for letter in key:
            my_hash = (my_hash + ord(letter)*23) % len(self.data_map)
        return my_hash

    def set_item(self, key, value):
        index = self.__hash(key)        
        if self.data_map[index] is None:    
            self.data_map[index] = []
        for bucket in self.data_map[index]:
            if key == bucket[0]: #check if the key already exists, if yes overwrite the value
                bucket[1] = value if value != bucket[1]  else bucket[1]
                return
        self.data_map[index].append([key,value])

    def print(self):
        for i,val in enumerate(self.data_map):
            print(i,": ",val)
    
    def get_item(self, key):
        index = self.__hash(key)
        if self.data_map[index] is None:
            return None
        elif len(self.data_map[index]) > 1:
            for item in self.data_map[index]:
                if item[0] == key:
                    return item[1]
        else:
            # as the individual index contains list of list, so self.data_map[index] points to list of list
            # and self.data_map[index][0] points to first list and as the list contains (key,value) so
            # we use self.data_map[index][0][1] to access the value contained in the first & only list
            # when there is no collision
            return self.data_map[index][0][1]

    def keys(self):        
        if self.data_map is None:
            return None
        else:
            keys_list = []
            for bucket in self.data_map:
                if bucket is not None:
                    for item in bucket:
                        keys_list.append(item[0])
        return keys_list

if __name__=="__main__":
    ht = HashTable(7)
    ht.set_item('nails',1000)
    ht.set_item('nails',1000)
    ht.set_item('nails',2000)
    ht.set_item('washers',50)
    ht.set_item('bolts',300)
    ht.print()
    print(ht.get_item('hello'))
    print(ht.get_item('bolts'))
    print(ht.get_item('nails'))
    print(ht.keys())
    mylist1 = []
    mylist2 = []
    newlist = [1,2]
    newlist2 = [1,2]
    mylist1.append(newlist)
    mylist1.append(newlist2)
    mylist2.extend(newlist)
    mylist2.extend(newlist2)
    print("mylist1 is = {}".format(mylist1))
    print("mylist2 is = {}".format(mylist2))
