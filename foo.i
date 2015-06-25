%module foo

%{
#define SWIG_FILE_WITH_INIT
#include "foo.hxx"
%}

%include <attribute.i>

%attributeref(Foo, int, a);

%include "foo.hxx"
