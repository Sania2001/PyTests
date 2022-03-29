import Calc
import pytest

@pytest.mark.parametrize("a,b,c",[(3,2,5),(5,6,11),(4,5,6)])
def test_add(a,b,c):
    # x =10
    # y =20
    result = Calc.add(a,b)
    assert c == result

@pytest.mark.parametrize("a,b,c",[(5,3,2),(11,5,6),(4,5,6)])
def test_sub(a,b,c):
    # x =20
    # y =10
    result = Calc.sub(a,b)
    assert c == result

@pytest.mark.parametrize("a,b,c",[(5,3,15),(11,5,55),(4,5,6)])
def test_mul(a,b,c):
    # x = 20
    # y = 10
    result = Calc.mul(a, b)
    assert c == result

@pytest.mark.parametrize("a,b,c",[(4,2,2),(36,6,6),(4,5,6)])
def test_div(a,b,c):
    # x = 20
    # y = 10
    result = Calc.div(a, b)
    assert c == result