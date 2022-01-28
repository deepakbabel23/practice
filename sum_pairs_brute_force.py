
def sum_pairs(arr, target):
    for i, elem in enumerate(arr):
        #print("index of {} is = {}".format(i, elem))
        number_to_find = target - elem
        for j in range(i+1, len(arr)):
            if arr[j] == number_to_find:
                print("Hurray!! Found an exact match")
                print("{} is the index of the pair {}".format([i, j], [arr[i],arr[j]]))
                return [i,j]
        #print("num = ", num)
    return "null"

def tc1():
    print("inside test case 1")
    arr = [ 2, 5, 8, 3, 6]
    target = 8
    return sum_pairs(arr, target)
def tc2():
    print("inside test case 2")
    arr = [6]
    target = 5
    return sum_pairs(arr, target)
def tc3():
    print("inside test case 3")
    arr = []
    target = 5
    return sum_pairs(arr, target)
def tc4():
    print("inside test case 4")
    arr = [19]
    target = 5
    return sum_pairs(arr, target)

if __name__=="__main__":
    print("TEST CASE passed") \
            if  "null" != tc1() \
            else print("test case failed")
    print("TEST CASE passed") \
            if  "null" != tc2() \
            else print("test case failed")
    print("TEST CASE passed") \
            if  "null" != tc3() \
            else print("test case failed")
    print("TEST CASE passed") \
            if  "null" != tc4() \
            else print("test case failed")