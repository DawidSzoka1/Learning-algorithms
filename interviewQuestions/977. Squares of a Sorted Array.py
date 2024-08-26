class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        a = [0] * len(nums)
        r = len(nums) -1
        l = 0
        c = len(nums) - 1
        while l <= r:
            po_r = nums[r] ** 2
            po_l = nums[l] ** 2
            if po_r > po_l:
                a[c] = po_r
                r -= 1
                c -= 1
            else:
                a[c] = po_l
                l += 1
                c -= 1
        return a
