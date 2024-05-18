class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        l = len(nums)
        i = 0
        once = []
        while i != l:
            if nums[i] in once:
                nums.remove(nums[i])
                l -= 1
            else:
                once.append(nums[i])
                i += 1
        return len(nums)
