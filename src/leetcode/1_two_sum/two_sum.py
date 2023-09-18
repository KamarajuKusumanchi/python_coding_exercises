from typing import List


# Keep the names of the class and function consistent with sample code in
# https://leetcode.com/problems/two-sum/description/
class Solution(object):
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        number_to_index_map = {}

        for index, number in enumerate(nums):
            complement = target - number
            if complement in number_to_index_map:
                complement_index = number_to_index_map[complement]
                return [complement_index, index]
            else:
                number_to_index_map[number] = index
