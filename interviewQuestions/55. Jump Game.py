class Solution:
    def canJump(self, nums: list[int]) -> bool:
        current = 0
        while True:
            jump = nums[current + nums[current]]
            print(jump)
            if nums.index(jump) == len(nums) - 1:
                return True
            current = nums.index(jump)
            if jump == 0:
                return False


print(Solution().canJump([2, 3, 1, 1, 4]))
