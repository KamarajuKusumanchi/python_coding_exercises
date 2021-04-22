from prime import is_prime
import pytest

@pytest.mark.parametrize("input,expected", [
    (-1, False),
    (2, True),
    (4, False),
    (5, True),
    (5.3, False)
])
def test_is_prime(input, expected):
    assert is_prime(input) == expected
