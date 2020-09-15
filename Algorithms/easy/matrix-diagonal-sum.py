class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n = len(mat)
        ans = sum([mat[i][i] + mat[i][n-i-1] for i in range(n)])
        if n % 2 == 1: return ans - mat[n//2][n//2]
        return ans