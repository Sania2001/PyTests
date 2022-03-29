import pytest
import area_rect_sq

@pytest.mark.skip(reason = "Currently skipped")
def test_area_rect():
    x =10
    y =20
    result = area_rect_sq.area_rect(x,y)
    assert x*y == result

@pytest.mark.myproject
def test_peri():
    x =10
    y =20
    result = area_rect_sq.pri_rect(x,y)
    assert x+x+y+y == result

@pytest.mark.myproject
def test_area_sq():
    x =10
    result = area_rect_sq.area_sq(x)
    assert x*x == result
