
def solution(A, K):
    # write your code in Python 3.6
    retVal = -1
    evenList = []
    oddList = []
    if not A: 
        return retVal
    if len(A) <K:
        return retVal
    if ((len(A) == 1) and (A[0] %2 !=0) ):
        return retVal
    if len(A) > 10000 or K > 100000:
        return -1
    sortedA = sorted(A,reverse=True)
    if A[0] > 100000:
        return -1
    for num in sortedA:
        if num%2 == 0:
            evenList.append(num)
        else:
            oddList.append(num)
    if not evenList:
        if (K %2 !=0):
            return -1
    mymax = 0
    evenIndex = 0
    oddIndex = 0
    for index in range(K-1):
        if (sortedA[index] %2 == 0):
            evenIndex +=1
        else:
            oddIndex +=1
    mymax = sum(sortedA[:K-1])
    if sortedA[K-1] %2 == 0:
        if ((len(evenList) >= evenIndex +1) and (len(oddList) >= oddIndex +1)):
            mymax = max((mymax - oddList[oddIndex -1] + sortedA[K-1] + evenList[evenIndex+1]),(mymax + oddList[oddIndex]))
        elif (len(evenList) < evenIndex +1):
            if (len(oddList) >= oddIndex +1):
              mymax = mymax + oddList[oddIndex]
            else:
                return -1
        elif (len(oddList) < oddIndex +1):
            if (len(evenList) >= evenIndex +1):
                mymax = mymax - oddList[oddIndex -1] + sortedA[K-1] + evenList[evenIndex+1]
            else:
                return -1
    else:
        if ((len(evenList) >= evenIndex +1) and (len(oddList) >= oddIndex +1)):
            mymax = max((mymax - evenList[evenIndex -1] + sortedA[K-1] + oddList[oddIndex+1]),(mymax + evenList[evenIndex]))
        elif (len(evenList) < evenIndex +1):
            if (len(oddList) >= oddIndex +1):
              mymax = mymax - evenList[evenIndex -1] + sortedA[K-1] + oddList[oddIndex+1]
            else:
                return -1
        elif (len(oddList) < oddIndex +1):
            if (len(evenList) >= evenIndex +1):
                mymax = mymax + evenList[evenIndex]
            else:
                return -1
    retVal = mymax
    return retVal
    
def t():
    nums = []
    k = 3
    print(solution(nums,k))
#t()

def tt():
    nums = [1,2]
    k = 3
    print(solution(nums,k))
#tt()

def ttt():
    nums = [1]
    k = 1
    print(solution(nums,k))
#tt()

def t1():
    nums = [4,9,8,2,6]
    k = 3
    print(solution(nums,k))
t1()

def t2():
    nums = [5,5,1,1,3]
    k = 3
    print(solution(nums,k))
t2()

def t3():
    nums = [4,2,6,7,8]
    k = 3
    print(solution(nums,k))
t3()

def t4():
    nums = [2,4,10,3,5]
    k = 3
    print(solution(nums,k))
t4()

def t5():
    nums = [7,7,7,7,7]
    k = 1
    print(solution(nums,k))

t5()
def t6():
    nums = [7,7,7,7,7]
    k = 3
    print(solution(nums,k))

t6()

def t7():
    nums = [13,12,10,8,7,6,4,1]
    k = 3
    print(solution(nums,k))
    #32
t7()

def t8():
    nums = [i for i in range(9999)]
    nums.append(10)
    nums.append(20)
    k = 3
    print(solution(nums,k))    
t8()

def t9():
    nums = [i for i in range(9999)]
    k = 10001
    print(solution(nums,k))    
t9()

def t10():
    nums = [200000,2,5,6,7,8]
    k = 3
    print(solution(nums,k))    
t10()