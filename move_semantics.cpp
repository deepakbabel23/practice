#include <iostream>
using namespace std;

class ArrayWrapper
{
public:
    // default constructor produces a moderately sized array
    ArrayWrapper()
        : _p_vals(new int[64])
        , _size(64)
    {}

    ArrayWrapper(int n)
        : _p_vals(new int[n])
        , _size(n)
    {}

    // move constructor
    ArrayWrapper(ArrayWrapper&& other)
        : _p_vals(other._p_vals)
        , _size(other._size)
    {
        std::cout << "Inside move constructor" << endl;
        other._p_vals = NULL;
        other._size = 0;
    }

    // copy constructor
    ArrayWrapper(const ArrayWrapper& other)
        : _p_vals(new int[other._size])
        , _size(other._size)
    {
        std::cout << "Inside copy constructor" << endl;
        for (int i = 0; i < _size; ++i)
        {
            _p_vals[i] = other._p_vals[i];
        }
    }
    ~ArrayWrapper()
    {
        std::cout << "in destructor" << endl;        
        delete[] _p_vals;
    }

private:
    int* _p_vals;
    int _size;
};

auto create_return_rval()
{
    ArrayWrapper obj1(5);
    return obj1;
}
auto create_return_lval()
{
    const ArrayWrapper obj1(5);
    return obj1;
}


int main4()
{
    
    ArrayWrapper obj2 = create_return_rval();    
    ArrayWrapper obj4 = create_return_lval();
    return 0;
}