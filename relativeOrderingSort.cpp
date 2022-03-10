// relativeOrderingSort.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include <iostream>
#include <unordered_map>
#include <map>
using namespace std;

class Solution {
public:
    vector<int> relativeSortArray(vector<int>& arr1, vector<int>& arr2) {
        //arr1 = [2,3,1,3,2,4,6,7,9,2,19]
        //arr2 = [2,1,4,3,9,6]
        //iterate over arr1 & count number of each distinct element present in arr2 in arr1
        //for remaining elements in arr1, count their occurrence and keep them in buckets

        std::unordered_map<int, int> arr2ElemMapInarr1;
        std::map<int, int> arr1RemElemMap;
        int arr1_size = arr1.size();
        int arr2_size = arr2.size();
        int arr2ElemMapInarr1_elem_cnt = 0;

        for (int i = 0; i < arr2_size; i++)
        {
            std::pair<int, int> pair(arr2[i], 0);
            arr2ElemMapInarr1.insert(pair);
        }
        //arr2ElemMapInarr1_elem_cnt = arr2ElemMapInarr1.size();
        for (int i = 0; i < arr1_size; i++)
        {
            //check if this element is also present in arr2's map
            if (arr2ElemMapInarr1.count(arr1[i]) != 0)
            {
                int existingCnt = arr2ElemMapInarr1[arr1[i]];
                arr2ElemMapInarr1[arr1[i]] = ++existingCnt;
                arr2ElemMapInarr1_elem_cnt++;
            }
            else // else this element is only present in arr1, so put it in new map
            {
                //check if we this is a repeated occurence of this element
                if (arr1RemElemMap.count(arr1[i]) != 0)
                {
                    int existingCnt = arr1RemElemMap[arr1[i]];
                    arr1RemElemMap[arr1[i]] = ++existingCnt;
                }
                else //element found first time, add it to the map with cnt as 1
                {
                    std::pair<int, int> pair(arr1[i], 1);
                    arr1RemElemMap.insert(pair);
                }
            }
        }
        //first iterate over arr2 array and for each element put it in arr1
        // as many times as it is in arr2 map
        for (int i = 0,j=0; i < arr2_size; i++)
        {
            std::unordered_map<int,int>::iterator iter =  arr2ElemMapInarr1.find(arr2[i]);
            int elemCnt = iter->second;
            for (int cnt = 0; cnt < elemCnt; cnt++)
            {
                arr1[j + cnt] = arr2[i];
            }
            j = j + elemCnt;
        }
        //for remaining elements copy elements with their respective 'cnt' times into
        //arr1 array
        int j = 0;
        for (auto& x : arr1RemElemMap)
        {
            //retrieving the count of this element..and that many times inserting it in the arr1
            int elemCnt = x.second;
            for (int cnt = 0; cnt < elemCnt; cnt++)
            {
                //remember to start filling from arr2ElemMapInarr1_elem_cnt bcoz
                //the previous is filled using the arr2Map elements
                arr1[arr2ElemMapInarr1_elem_cnt + j+cnt] = x.first;
            }
            j= j + elemCnt; //no of occurrences of this element + prevElementEndIndex
        }
        return arr1;
    }
};

int main()
{
    std::unordered_map<int, int> myrecipe1;
    myrecipe1.insert(std::make_pair<int, int>(1, 1));
    for (auto& x : myrecipe1)
        std::cout << x.first << " " << x.second << std::endl;
    std::vector<int> vec1({ 2, 3, 1, 3, 2, 4, 6, 7, 9, 2, 19,7,19 });
    std::vector<int> vec2({ 2, 1, 4, 3, 9, 6 });
    Solution sol1;
    sol1.relativeSortArray(vec1, vec2);
    std::cout << "Hello World!\n";
}

// Run program: Ctrl + F5 or Debug > Start Without Debugging menu
// Debug program: F5 or Debug > Start Debugging menu

// Tips for Getting Started: 
//   1. Use the Solution Explorer window to add/manage files
//   2. Use the Team Explorer window to connect to source control
//   3. Use the Output window to see build output and other messages
//   4. Use the Error List window to view errors
//   5. Go to Project > Add New Item to create new code files, or Project > Add Existing Item to add existing code files to the project
//   6. In the future, to open this project again, go to File > Open > Project and select the .sln file
