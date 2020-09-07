// negate i-1, if i-1 is already negative it's a duplicate
// works since 1 <= a[i] <= n, so i-1 will always be a valid index
// essentially boolean array with no extra space
class Solution {
    public List<Integer> findDuplicates(int[] nums) {
        List<Integer> ans = new ArrayList<>();
        for (int i = 0; i < nums.length; ++i) {
            int index = Math.abs(nums[i]) - 1;
            if (nums[index] < 0) ans.add(index + 1);
            else nums[index] *= -1;
        }
        return ans;
    }
}