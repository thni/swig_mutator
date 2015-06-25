# swig_mutator

How to wrap C++ getter/setter in Python with SWIG

Build with:

    ./waf configure
    ./waf build

Run the C++ program with:

    ./build/main

Run the Python script with:

    python main.py

# References

* [SWIG macros for  mutators](https://github.com/swig/swig/blob/master/Lib/typemaps/attribute.swg)
* [SWIG const-correctness](http://swig.org/Doc3.0/SWIGDocumentation.html#SWIGPlus_const)

# References

The waf executable has been created with:

    wget --no-check-certificate https://waf.io/waf-1.8.11.tar.bz2
    tar xvjf waf-1.8.11.tar.bz2
    cd waf-1.8.11/
    python waf-light  --make-waf --tool=swig
