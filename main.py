import sys
sys.path.append('build')

from foo import Foo

foo = Foo()
print foo.a
foo.a = 1
print foo.a
