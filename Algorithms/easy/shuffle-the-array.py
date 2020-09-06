class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        ans = []
        for x in range(n):
            ans.append(nums[x])
            ans.append(nums[x + n])
        return ans
