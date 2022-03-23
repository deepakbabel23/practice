def solution(A):
    # write your code in Python 3.6
    sorted_A = sorted(A)
    sorted_A = [element for element in sorted_A if element > 0 and element <=100000]
    sorted_A = set(sorted_A)
    if not sorted_A:
        return 1
    for index, element in enumerate(sorted_A):        
        if element != index+1:
            val = index+1
            return val
    val = max(sorted_A)+1
    return val

A = [1,3,6,4,2]

def test_case1():
    A = [1,3,6,4,2]
    print(solution(A))

def test_case2():
    A = [1,3,6,4,2,1]
    print(solution(A))

def test_case3():
    A = [1,3,6,4,2,0]
    print(solution(A))

def test_case4():
    A = [-5, -4 ,3,6,4,2,0]
    print(solution(A))

def test_case5():
    A = [-200000,3,1,4,2,2000000, 99999]
    print(solution(A))

def test_case6():
    A = [0,3,1,2]
    print(solution(A))

test_case1()
test_case2()
test_case3()
test_case4()
test_case5()
test_case6()

#1,2,3,4,6
#0 1 2 3 4