#Given an input string, reverse the string word by word

from re import match
from typing import Match


def reverse_string_word_by_word(input_sentence):
    input_list = input_sentence.split(" ")
    length = len(input_list)    
    mid = int(length/2)
    for index in range(0,mid):
        input_list[index],input_list[length-index-1] = input_list[length-index-1], input_list[index]
    print(input_list)

sentence = "Given an input string reverse the string word by word"
print(sentence)
reverse_string_word_by_word(sentence)

"""
Given an array of integers nums and an integer target, 
return indices of the two numbers such that they add up to target. 
You may assume that each input would have exactly one solution, 
and you may not use the same element twice
nums = [3,3,7,2,5,1,6,8]
(3) = () //as 3+3 = 6..no duplicates allowed
(3) = () //as 3+3 = 6..no duplicates allowed
7=> (-1) not in (2,5,1,6,8)
2 => (4) not in (5,1,6,8)
5 => (1) in (1,6,8) => return the pair
target = 6
Output = (1,4)
"""

def return_sum_pair(nums, int_target):    
    if not nums:
        return ()
    map_to_find_matching_number = None
    mymap = dict()
    for index, num in enumerate(nums):
        mymap[num] = index
    
    for index, num in enumerate(nums):        
        matching_number_of_pair = int_target - num;
        if matching_number_of_pair == num:
            continue
        remaining_tuple_keys = (nums[index+1:])
        d1 = {k:mymap[k] for k in remaining_tuple_keys}
        if d1.get(matching_number_of_pair):
            ind = d1.get(matching_number_of_pair)
            return (index, ind)
        #for j in range(index+1, len(nums)):
        #    if nums[j] == num:
        #        continue
        #    if nums[j] == matching_number_of_pair:
        #        index_pair =  (index,j)
        #        return index_pair


nums = [3,1,3,7,5,6]

def test_case1():
    target = 6
    print(return_sum_pair(nums,target))
    #Output: (1,4)

def test_case2():
    target = 11
    print(return_sum_pair(nums,target))
    #Output: (4,5)

def test_case3():
    target = 6
    nums = []
    print(return_sum_pair(nums,target))
    #Output: ()

def test_case4():
    target = -20
    nums = [-20,-10,5,-10,20,-25]
    print(return_sum_pair(nums,target))
    #Output: (2,5)

test_case1()
test_case2()
test_case3()
test_case4()