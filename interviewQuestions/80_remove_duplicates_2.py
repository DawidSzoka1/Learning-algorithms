class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        for i in nums:
            while nums.count(i) > 2:
                nums.remove(i)
        return len(nums)


nums = [0, 0, 0, 0, 0]
Solution().removeDuplicates(nums)
print(nums)
