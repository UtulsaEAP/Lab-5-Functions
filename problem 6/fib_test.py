from fib import fibonacci

error_msg = "The input is the index in the fibonacci sequence, the output is the value at that index."

def test_fibonacci_7():
    assert fibonacci(7) == 13, error_msg

def test_fibonacci_0():
    assert fibonacci(0) == 0, error_msg

def test_fibonacci_2():
    assert fibonacci(2) == 1, error_msg

def test_fibonacci_1():
    assert fibonacci(1) == 1, error_msg

def test_fibonacci_10():
    assert fibonacci(10) == 55, error_msg

def test_fibonacci_5():
    assert fibonacci(5) == 5, error_msg
