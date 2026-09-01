class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        output = {}

        for index, num in enumerate(nums):
            remaining_n = target - num
            if remaining_n in output:
                return [output[remaining_n], index]
            output[num] = index