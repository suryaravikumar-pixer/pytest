import math_func
import pytest
import sys
# sys going to give informaiton about the python version running
# @pytest.mark.skip(reason="skip this test")
@pytest.mark.skipif(sys.version_info < (3, 3), reason="version is outdated i.e. 3.3s")
def test_add():
    assert math_func.add(7,3) == 10
    assert math_func.add(7,6) == 13
    assert math_func.add(5,9) == 14


def test_product():
    assert math_func.product(3,3) == 9
    assert math_func.product(3,4) == 12
    assert math_func.product(3,7) == 21


def test_add_strings():
    result = math_func.add('Hello', ' World')
    assert result == 'Hello World'
    assert type(result) is str
    assert 'Heldlo' not in result


def test_product_strings():
    assert math_func.product('Hello ', 3) == 'Hello Hello Hello '
    result = math_func.product('Hello ')
    assert result == 'Hello Hello '
    assert type(result) is str
    assert 'Hello' in result 