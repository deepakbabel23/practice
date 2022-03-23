#primitive types like integer are immutable
import copy
from copy import deepcopy

num1 = 10
num2 = num1

print("before updating")
print(f"value of num1 is {num1}")
print(f"value of num2 is {num2}")

print(f"id(num1) is {id(num1)}")
print(f"id(num2) is {id(num2)}")
print(f"address of integer object contained in num1 is {id(10)}")

num2 = 20

print("after updation")

print(f"value of num1 is {num1}")
print(f"value of num2 is {num2}")

print(f"id(num1) is {id(num1)}")
print(f"id(num2) is {id(num2)}")

print(f"address of integer object {num1} contained in num1 is {id(10)}")
print(f"address of integer object {num2} contained in num2 is {id(20)}")


list1 = [1,2,3,4]
list2 = list1
# list2 = list1.copy() # for deep copying immutable objects inside this container
#Methods:pop(elemIndex),pop(),remove(),count(),index(elem),append(elem),insert(index,elem),extend(newList),sort,reverse
#Indexable(access element by Index), Iterable(one after another), Mutable(contents can be changed),non hashable
print("before updation")
print(f"address of mylist is = {id(list1)}")
print(f"address of mylist2 is = {id(list2)}")

print(f"value of list1 is = {list1}")
print(f"value of list2 is = {list2}")

#changing contents of list2
#this shows list are mutable
list2[2] = 10
print("after updation")
print(f"address of list1 is {id(list1)}")
print(f"address of list2 is {id(list2)}")

print(f"value of list1 is = {list1}")
print(f"value of list2 is = {list2}")

list3 = [4,5,1,[9,3]]
print(f"pointing list2 to another list list3")
list2 = list3

print("after pointer updation")
print(f"address of list1 is {id(list1)}")
print(f"address of list2 is {id(list2)}")
print(f"address of list3 is {id(list3)}")

print(f"value of list1 is = {list1}")
print(f"value of list2 is = {list2}")
print(f"value of list3 is = {list3}")

tupp = 1,
print(type(tupp))
tuple1 = (1,22,13)
tuple2 = tuple1
#tuple2 = tuple1.copy() method is not present as its immutable already
#Methods: count(element),index(element)
#Indexable(access element by Index), iterable(access element one after other), immutable(contents can't be changed),
#hashable(as its immutable)
#Iterable example
#basically comma operator is used to identify that given set of python elements is a tuple or not. () is optional
#and  only required if the tuple is empty
for index in range(len(tuple1)):
    print(tuple1[index])
#Indexable example
print(tuple1[0])
print("before updation")
print(f"address of tuple1 is = {id(tuple1)}")
print(f"address of tuple2 is = {id(tuple2)}")

print(f"value of tuple1 is = {tuple1}")
print(f"value of tuple2 is = {tuple2}")
# tuple is immutable, so we can't modify contents of tuple..this line will throw error
# also no method exists in tuple class to modify contents of a tuple
#tuple2[1] = 5

#But we can change use the same tuple name variable to refer to a new tuple
# by assigning a address location to existing tuple variable
#using pointers assignment
tuple3 = (1,5,[7])
tuple2 = tuple3
print("pointing tuple2 to tuple3..after updation")
print(f"address of tuple1 is = {id(tuple1)}")
print(f"address of tuple2 is = {id(tuple2)}")
print(f"address of tuple3 is = {id(tuple3)}")

print(f"value of tuple1 is = {tuple1}")
print(f"value of tuple2 is = {tuple2}")
print(f"value of tuple3 is = {tuple3}")

print("before updation")
print(f"third element of tuple is = {tuple3[2]}")
print("after updation")
tuple3[2].append({"dict_key":"value"})
dict9 = dict({"dict_key":"value"})
print(f"third element of tuple is = {tuple3[2]}")

set1 = {1,2,3}
set2 = set1
#set2 = set1.copy() # for deep copying immutable objects inside this container
#Non Indexable(no relation between current Element and next Element), Non iterable(as its not indexable)
print("before updation")
print(f"address of set1 is = {id(set1)}")
print(f"address of set2 is = {id(set2)}")

print(f"value of set1 is = {set1}")
print(f"value of set2 is = {set2}")

#lets try to change set contents
set2.discard(2)
set1.add(55)

print("after updation")
print(f"address of set1 is = {id(set1)}")
print(f"address of set2 is = {id(set2)}")

print(f"value of set1 is = {set1}")
print(f"value of set2 is = {set2}")

#set2 will now point to set3
set3 = {4,10,90}
set2 = set3

print("after updation")
print(f"address of set1 is = {id(set1)}")
print(f"address of set2 is = {id(set2)}")
print(f"address of set3 is = {id(set3)}")

print(f"value of set1 is = {set1}")
print(f"value of set2 is = {set2}")
print(f"value of set3 is = {set3}")

dict1 = {"val":1}
dict2 = dict1

print("before updation")
print(f"address of dict1 is = {id(dict1)}")
print(f"address of dict2 is = {id(dict2)}")

#changing contents of dict2
#this shows dictionaries are mutable
dict2["val"] = 2
print(f"address of dict2 is = {id(dict2)}")
print(f"address of dict1 is = {id(dict1)}")

print("after updation value by changing contents through pointer")
print(f"value of dict1 is {dict1}")
print(f"value of dict2 is {dict2}")

print("pointer assignment to point dict2 to dict3")
dict3 = {"val":3}
dict2 = dict3
#dict2 = dict3.copy() #for deep copying immutable objects inside this container

print("after update")
print(f"value of dict1 is {dict1}")
print(f"value of dict2 is {dict2}")
print(f"value of dict3 is {dict3}")

print("after updation")
print(f"address of dict1 is {id(dict1)}")
print(f"address of dict2 is {id(dict2)}")
print(f"address of dict3 is {id(dict3)}")

#Note: Only tuples are immutable in python, rest all data structures are mutable

#Iterable - an object whose elements are arranged in contiguous format or it provided ability to reach next element
#from current element
#eg. List, Tuple, String

#Hashable - Immutable objects whose value does not change, can be hashed.eg. all built-in python objects,strings,tuple
#These objects can act as "key" for hashable data structures like set and dict in python
#Mutable objects like List,Set,Dict can't act as keys in Hashabled DS(eg. Set, Dict) as their values can be changed
