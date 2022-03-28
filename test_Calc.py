import Calc

def test_add():
    x =10
    y =20
    result = Calc.add(x,y)
    assert x+y == result

def test_sub():
    x =20
    y =10
    result = Calc.sub(x,y)
    assert x-y == result

def test_mul():
    x = 20
    y = 10
    result = Calc.mul(x, y)
    assert x * y == result

def test_div():
    x = 20
    y = 10
    result = Calc.div(x, y)
    assert x / y == result