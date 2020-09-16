# O(n), dictionary
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        seen = {}
        ans = 0
        for x in nums:
            if x in seen:
                ans += seen[x]
                seen[x] += 1
            else:
                seen[x] = 1
        return ans

""" naive O(n^2), check all pairs
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        ans = 0
        n = len(nums)
        for i in range(n):
            for j in range(i+1,n):
                if nums[i] == nums[j]:
                    ans += 1
        return ans
"""