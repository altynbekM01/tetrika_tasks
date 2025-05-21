import pytest
from task_1.solution import sum_two

def test_sum_two_valid():
    assert sum_two(1, 2) == 3

def test_sum_two_invalid_type():
    with pytest.raises(TypeError) as excinfo:
        sum_two(1, 2.4)
    assert "Argument 'b' must be of type int" in str(excinfo.value)
