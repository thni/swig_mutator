#include <iostream>

#include "foo.hxx"

using namespace std;
int main()
{
    Foo foo;
    cout << foo.a() << endl;
    foo.a() = 1;
    cout << foo.a() << endl;
}
