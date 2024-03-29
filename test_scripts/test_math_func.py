#from unit_testing.pytest_folder import math_func
#!/usr/bin/python3
from files import math_func
#imported the above libraries from executing the script


def test_add():
    print("--")
    assert math_func.add(7, 3) == 10
    assert math_func.add(7) == 9
    assert math_func.add(3) == 5


def test_prod():
    assert math_func.prod(2, 4) != 81
    assert math_func.prod(4) == 8
    assert math_func.prod(6, 4) == 24

