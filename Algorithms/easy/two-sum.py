# O(n)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {} # key is num, val is index
        for i in range(len(nums)):
            x = target - nums[i]
            if x in seen:
                return [i, seen[x]]
            seen[nums[i]] = i