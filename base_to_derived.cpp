#include <iostream>
using namespace std;

class Base {
	public:
		void F1() { /*cout << "Base F1" << endl;*/  F2(); }
		virtual void F2() { cout << "Base F2" << endl; }
		void F3() { cout << "Base F3" << endl; }
};

class Der1 : public Base {
	public:
	void F2() { cout << "Der1 F2" << endl; }
	void F3() { cout << "Der1 F3" << endl; }
	void F4() { cout << "Der1 F4" << endl; }
};

class Der2 : public Base {
public:
	void F2() { cout << "Der2 F2" << endl; }
	void F3() { cout << "Der2 F3" << endl; }
};

int main3() {
	Der1 d1;
	d1.F1(); //D1 F1
	Der2 d2;
	d2.F1(); //D2 F1
	Base b1 = d1;
	b1.F2(); //B1 F2
	//
	////with base class pointer, call depends on address of object contained in base class pointer
	//Base* b2 = &d1;
	//b2->F2();
	Base b3 = d1;
	cout << "calling Base b3 = d1; b3.F3()" << endl;
	b3.F3();
	////without using virtual functions with base class pointer, the call depends on type of pointer
	//Base* b4 = &d1;
	//b4->F3();
	return 0;
}