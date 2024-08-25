class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        has_map = {}
        for i in range(len(nums)):
            if nums[i] not in has_map:
                has_map[nums[i]] = i
            else:
                has_map[nums[i]] = i

        for i in range(len(nums)):
            looking_for = target - nums[i]
            if looking_for in has_map:
                if i != has_map[looking_for]:
                    return [i, has_map[looking_for]]
