#include <iostream>
#include <vector>
using namespace std;


class Solution2 {
public:
    int splitArray(vector<int>& nums, int m) {
    //Input: nums = [7, 2, 5, 10, 8], m = 2
    //Output : 18

    //Input : nums = [1, 4, 2], m = 2
    //Output : 4

    //Input : nums = [1, 4, 4], m = 2
    //Output : 5  ..note max_sum could have been 8(4+4), but we divided it
    //into [1,4] & [4] to obtain minimum largest sum

    //Input : nums = [7, 2, 5, 10, 8], m = 2
    //Output : 4
        return 0;
    }
};

int main2()
{
    Solution2 sol2;
    std::vector<int> vec1({ 7,2,5,10,8 });
    int m = 2;
    int largest_sum_subarray = sol2.splitArray(vec1, m);
    cout << endl;
    cout << "largest_sum_subarray is = : " << largest_sum_subarray << endl;
    return 0;
}