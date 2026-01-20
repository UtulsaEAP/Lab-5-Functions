# Import student module you would like to test.
# For example:
# from main import add

from intToBin import int_to_reverse_binary, string_reverse

func_error = "Ensure that you are using both functions to perform the task."
def test_int_to_reverse_binary():
    assert int_to_reverse_binary(19) == "11001", func_error
    assert int_to_reverse_binary(255) == "11111111", func_error
    assert int_to_reverse_binary(122) == "0101111", func_error
    assert int_to_reverse_binary(0) == "0", func_error
    assert int_to_reverse_binary(1) == "1", func_error

def test_string_reverse():
    assert string_reverse("11001") == "10011", func_error
    assert string_reverse("11111111") == "11111111", func_error
    assert string_reverse("0101111") == "1111010", func_error
    assert string_reverse("0") == "0", func_error
    assert string_reverse("1") == "1", func_error

