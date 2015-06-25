#! /usr/bin/env python

top = '.'
out = 'build'

def options(opt):
    opt.load('g++ python')

def configure(conf):
    conf.load('g++ python')
    conf.check_python_version((2,4,2))
    conf.check_python_headers()

    conf.load('swig')
    if conf.check_swig_version() < (1, 2, 27):
        conf.fatal('this swig version is too old')

def build(bld):

    bld.shlib(
        features = 'cxx',
        source = 'foo.cxx',
        target = 'foo',
        includes = '.',
        export_includes = '.',
        name = 'FOO'
    )

    bld.program(
        source = 'main.cxx',
        target = 'main',
        use = ['FOO'],
        rpath = ['$ORIGIN'],
    )

    bld(
        features = 'cxx cxxshlib pyext',
        source = 'foo.i',
        target = '_foo',
        swig_flags = '-c++ -python -Wall',
        includes = '.',
        use  = 'FOO',
        rpath = ['$ORIGIN', ],
     )

