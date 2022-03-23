
import sys
print(sys.version)
print("hello world")

def complexity_n(n):
    for i in range(n):
        print(i)
    for j in range(n):
        print(j)
    print("function complexity is = O({})".format(n))

complexity_n(5)

def complexity_ab(a,b):
    for i in range(a):
        print(i)
    for j in range(b):
        print(j)
    print("function complexity is O({}+{})".format(a,b))

complexity_ab(2,3)

def complexity_n2(n):
    for i in range(n):
        for j in range(n):
            print(i*j)
    print("function complexity is O({}2)".format(n))

complexity_n2(5)

def complexity_ab(a,b):
    for i in range(a):
        for j in range(b):
            print(a*b)
    print("function complexity is O({}*{})".format(a,b))

complexity_ab(2,3)