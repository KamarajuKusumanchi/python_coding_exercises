from typing import List
import pytest
from two_sum import Solution


@pytest.mark.parametrize(
    "nums, target, expected_result",
    [
        ([2, 7, 11, 15], 9, [0, 1]),
        ([3, 2, 4], 6, [1, 2]),
        ([3, 3], 6, [0, 1]),
        ([3, 5, 1, 4, -8], 5, [2, 3]),
    ],
)
def test_two_sum(nums: List[int], target: int, expected_result: List[int]) -> None:
    actual_result = Solution().twoSum(nums, target)
    assert actual_result == expected_result
