

from stepCounter import feet_to_steps

int_error = "Ensure that you typecast to int. (How is this different than rounding?)"
def test_feet_to_steps():
    # Test case 1
    assert feet_to_steps(11) == int(11 / 2.5), int_error
    
    # Test case 2
    assert feet_to_steps(79.25) == int(79.25 / 2.5), int_error
    
    # Test case 3
    assert feet_to_steps(150.5) == int(150.5 / 2.5), int_error
    
    # Additional test cases
    # Test case 4
    assert feet_to_steps(0) == int(0 / 2.5), int_error
    
    # Test case 5
    assert feet_to_steps(2.5) == int(2.5 / 2.5), int_error
    
    # Test case 6
    assert feet_to_steps(10000) == int(10000 / 2.5), int_error
