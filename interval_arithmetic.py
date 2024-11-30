import numbers

class NumberRange:
    def __init__(self, begin, end):
        self.begin = begin
        self.end = end

    def __add__(self, other):
        if isinstance(other, NumberRange):
            return radd(self, other)
        if isinstance(other, numbers.Number):
            r = rnumber(other)
            return radd(self, r)
        raise TypeError("ivalid type")

    def __radd__(self, other):
        if isinstance(other, numbers.Number):
            return radd(self, rnumber(other))
        raise TypeError("ivalid type")


    def __sub__(self, other):
        if isinstance(other, NumberRange):
            return rsub(self, other)
        if isinstance(other, numbers.Number):
            r = rnumber(other)
            return rsub(self, r)
        raise TypeError("ivalid type")

    def __rsub__(self, other):
        if isinstance(other, numbers.Number):
            return rsub(self, rnumber(other))
        raise TypeError("ivalid type")

    def __mul__(self, other):
        if isinstance(other, NumberRange):
            return rmul(self, other)
        if isinstance(other, numbers.Number):
            r = rnumber(other)
            return rmul(self, r)
        raise TypeError("ivalid type")

    def __rmul__(self, other):
        if isinstance(other, numbers.Number):
            return rmul(self, rnumber(other))
        raise TypeError("ivalid type")

    def __truediv__(self, other):
        if isinstance(other, NumberRange):
            return rdiv(self, other)
        if isinstance(other, numbers.Number):
            r = rnumber(other)
            return rdiv(self, r)
        raise TypeError("ivalid type")

    def __rtruediv__(self, other):
        if isinstance(other, numbers.Number):
            return rdiv(self, rnumber(other))
        raise TypeError("ivalid type")


class In(NumberRange):
    def __init__(self, begin, end):
        assert(begin <= end)
        NumberRange.__init__(self, begin, end)
    def __repr__(self):
        return f"In({self.begin},{self.end})"

class Out(NumberRange):
    def __init__(self, begin, end):
        NumberRange.__init__(self, begin, end)
    def __repr__(self):
        return f"Out({self.begin},{self.end})"


def radd(a, b):
    '''
    in + out:
    a < x < b     and    (y < c or d < y)
    a + d < x + y   or   x + y < b + c

    out + out:
    (x < a or b < x)  and  (y < c or d < y)
    x + y < a + c  or b + d < x + y or unrestricted or unrestricted
    unrestricted
    '''
    if isinstance(a, In) and isinstance(b, In):
        return In(a.begin+b.begin, a.end+b.end)
    if isinstance(a, Out) and isinstance(b, Out):
        return Out(0,0) #unrestricted
    if isinstance(a,In) and isinstance(b, Out):
        return Out(a.end + b.begin, a.begin + b.end)
    if isinstance(a, Out) and isinstance(b, In):
        return Out(a.begin + b.end, a.end + b.begin)

    assert(0 and "not implemented")

def rnumber(a):
    return In(a, a)

def rneg(a):
    if isinstance(a, In):
        return In(-a.end, -a.begin)
    if isinstance(a, Out):
        return Out(-a.end, -a.begin)

def rsub(a,b):
    '''
    ab < x < ae       bb < y < be

    ab - be < x - y < ae - ab
    '''
    return radd(a, rneg(b))

def rmul(a,b):
    if isinstance(a, In) and isinstance(b, In):
        l = []
        l.append(a.begin * b.begin)
        l.append(a.begin * b.end)
        l.append(a.end   * b.begin)
        l.append(a.end   * b.end)
        return In(min(l), max(l))

# def rdiv(a,b):
#     if isinstance(a, In) and isinstance(b, In):

def rinv(a):
    if isinstance(a, In):
        if a.begin > 0 or a.end < 0:
            return In(1/a.end, 1/a.begin)
        else:
            return Out(1/a.begin, 1/a.end)
    if isinstance(a, Out):
        if a.begin > 0 or a.end < 0:
            return Out(1/a.end, 1/a.begin)
        else:
            return In(1/a.begin, 1/a.end)

def rdiv(a,b):
    return rmul(a, rinv(b))

def res(v, tol=0.05):
    return In(v*(1-tol), v*(1+tol))

def out2(v1, r1, v2, r2):
    return (v1/r1 + v2/r2)/(1/r1 + 1/r2)

