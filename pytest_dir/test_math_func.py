import math_func
# in order to recognize the function use test followd by name(test_add, test_product)

def test_add():
    assert math_func.add(7,3) == 10
    assert math_func.add(7) == 9
    assert math_func.add(5) == 7

def test_product():
    assert math_func.product(3,3) == 9
    assert math_func.product(3,) == 6
    assert math_func.product(3,7) == 21
