from interval_arithmetic import *

def test1():
    print(In(3,4))
    print(In(-1,9))
    # print(In(10,5)) invalid interval
    print(Out(1,5))

    a = In(1,3)
    b = In(10,20)
    c = In(500,600)

    print(radd(a,b))
    print(radd(a,c))

    d = In(-3, 3)
    e = In(-5, 4)
    f = In(-5,-2)

    print(rmul(b,d))
    print(rmul(d,e))

    print(rinv(a))
    print(rinv(f))
    print(rinv(e))

def test2():
    a = In(1,3)
    b = Out(-1,1)

    print(radd(a,b))

def test3():
    r1 = res(1500)
    r2 = res(3000)
    Vi = In(6,6)
    t1 = radd(r1, r2)
    t2 = rdiv(r1, t1)
    print(f"{t1=}")
    print(f"{t2=}")
    Vo = rmul(Vi, t2)
    print(Vo)

    low  = out2(6, r2.end, 0, r1.begin)
    high = out2(6, r2.begin, 0, r1.end)
    print(f"{low=}, {high=}")

def test4():
    x = In(0,1)
    one = In(1,1)

    r = rmul(x, rsub(one, x))
    print(f"{r=}")

def test5():
    r1 = res(1500)
    r2 = res(3000)
    Vi = In(6,6)
    Vo = rmul(Vi, rinv(radd(In(1,1), rdiv(r2,r1))))
    print(Vo)

    low  = out2(6, r2.end, 0, r1.begin)
    high = out2(6, r2.begin, 0, r1.end)
    print(f"{low=}, {high=}")

def test6():
    x = In(0,1)
    half = In(1/2,1/2)
    quarter = In(1/4,1/4)

    t1 = rsub(x, half)
    t2 = rmul(t1, t1)
    print(f"{t2=}")
    r = rsub(quarter, t2)
    print(f"{r=}")

def test7():
    x = In(-1,1)

    #f(x) = x²
    f = rmul(x,x)
    print(f"{f=}")
    # we would expect the smallest output value
    # would be 0, because x² can not produce negative
    # values (we are not considering complex numbers)
    # but because there is no coupling, it's like
    # f = x1 * x2, the smalles value for f is
    # obtained for, say x1 = 1 and x2 = -1

def test8():
    t1 = In(1,2) + 3
    print(f"{t1=}")
    t2 = 4.0 + In(1,2)
    print(f"{t2=}")

if __name__ == '__main__':
    test1()
    test2()
    test3()
    test4()
    test5()
    test6()
    test7()
    test8()