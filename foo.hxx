#ifndef FOO_INCLUDED_HPP
#define FOO_INCLUDED_HPP

class Foo
{
    public:
        Foo();

        const int &
        a() const;

        int &
        a();

    private:
        int m_a;
};

inline
int const & Foo::a() const
{ return m_a; }

inline
int & Foo::a()
{ return m_a; }

#endif
