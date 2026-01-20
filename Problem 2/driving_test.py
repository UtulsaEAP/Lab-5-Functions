# from main import add
from driving import driving_cost
import pytest

student_result = ''
func_error = "Function call to driving_cost did not return a value. Ensure that the function returns the appropriate value"
val_error = f"Function call to driving_cost incorrectly returned {student_result}. Verify units."
def test_driving_cost_case1():
    student_result = driving_cost(20.0, 3.1599, 10.0)
    assert student_result is not None, func_error
    assert abs(student_result - 1.57995) < 0.001, val_error

def test_driving_cost_case2():
    student_result = driving_cost(20.0, 3.1599, 50.0)
    assert student_result is not None, func_error
    assert abs(student_result - 7.89975) < 0.001, val_error

def test_driving_cost_case3():
    student_result = driving_cost(20.0, 3.1599, 400.0)
    assert student_result is not None, func_error
    assert abs(student_result - 63.198) < 0.001, val_error

def test_driving_cost_case4():
    student_result = driving_cost(25.0, 3.50, 100.0)
    assert student_result is not None, func_error
    assert abs(student_result - 14.0) < 0.001, val_error

def test_driving_cost_case5():
    student_result = driving_cost(15.0, 4.00, 150.0)
    assert student_result is not None, func_error
    assert abs(student_result - 40.0) < 0.001, val_error
