class Solution:
    def search(self, nums: list[int], target: int) -> int:
        l, r, mid = 0, len(nums) - 1, 0
        while l <= r:
            mid = l + ((r -l) // 2)
            print(mid)
            if nums[mid] == target:
                return mid
            if nums[mid] >= nums[l]:
                if (target < nums[l] or target > nums[mid]):
                    l = mid + 1
                else:
                    r = mid - 1
            else:
                if (target <= nums[mid] or target > nums[r]):
                    r = mid - 1
                else:
                    l = mid + 1
        return -1
        