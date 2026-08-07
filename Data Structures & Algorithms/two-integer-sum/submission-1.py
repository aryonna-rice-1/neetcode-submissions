from collections import defaultdict
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        indexes = defaultdict(list)
        for i in range(len(nums)):
            indexes[nums[i]].append(i)

        for i in range(len(nums)):
            other = target - nums[i]
            other_indexes = indexes.get(other)
            if other_indexes:
                if i in set(other_indexes):
                    if len(other_indexes) > 1:
                        return [i, other_indexes[-1]]
                else:
                    return [i, other_indexes[-1]]
        return []