class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        output = {}

        for index, num in enumerate(nums):
            second_num = target - num
            if second_num in output:
                return [output[second_num], index]
            output[num] = index