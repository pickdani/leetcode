# looks at each log once so O(n), where n is len(logs)
class Solution:
    def minOperations(self, logs: List[str]) -> int:
        ans = 0
        for x in logs:
            if x == "../":
                ans = max(0, ans - 1)
            elif x != "./":
                ans +=1
        return ans