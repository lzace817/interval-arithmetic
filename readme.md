# interval arithmetic
This is based on a lecture from [professor's Wildberger youtube chanel](https://www.youtube.com/@njwildberger).

interval arithmetic allow us to do computations using intervals. The semantics for a operation is: a math operation with intervals is the range of the function defined by applying the same operation to a independent set of variables, each variable correspoding to a interval defining its domain.

## example

`In(1, 2) + In(30, 40)` is equal to `In(31, 42)` because if `x` have domain `[1 .. 2]` and `y` have domain `[30 .. 40]`, then `x+y` will have range `[31 .. 42]`

## quick start

``` python
$ python3
>>> from interval_arithmetic import *
>>> In(10,20) - In(3,4)
In(6,17)
```

## limitation
turns out we can not do interval _algebra_ because variables do not "couple".

let `f(x) = x*(1-x)` and `x in [0 .. 1]`. The range of `f` is in `[0 .. 1/4]` but `In(0, 1) * (In(1, 1) - In(0, 1)) = In(0, 1)`. It contains the range, but it is not thight.