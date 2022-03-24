#include <iostream>
#include <vector>
#include <stack>
using namespace std;


//Sequence of words (dont' reverse characters, but print words in reverse format)
//Input: i am a programmer
//Output: programmer am i

void reverse(std::string& input_str)
{
	cout << "the original string is: " << input_str << endl;
	std::stack<std::string> mystack = {};	
	// logic for reversing
	//take all the items in reverse order into temp_str
	
	std::vector<char> vec = {};
	for (auto& item : input_str)
	{	
		//item;
		if (' '== item)
		{
			auto str = vec.data();
			mystack.push(str);
			vec.clear();
		}
		else
		{
			vec.push_back(item);			
		}
		cout << "item is = :" << item << endl;
	}
	mystack.push(vec.data());
	auto size = mystack.size();
	for (int i = 0; i < size; i++)
	{
		cout << mystack.top() << endl;
		mystack.pop();
	}

	//another approach
	//two pointers, first pointing to initial word/character, second pointer point to the last character/word
	// i =0, l = strlen(str)
	//i am a programmer
	//f => i//programmer
	//l => programmer

}


//





















int main6()
{
	std::string input_str = "i am a programmer";
	reverse(input_str);
	cout << "the reversed string is: " << input_str << endl;
	return 0;
}