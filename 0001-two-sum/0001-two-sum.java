class Solution {
    public int[] twoSum(int[] nums, int target) {
        ArrayList<Integer> results = new ArrayList<>();

        for (int i = 0; i < nums.length; i++) {
            for (int j = i + 1; j < nums.length; j++) {
                if (target == nums[i] + nums[j]) {
                                return new int[] {i, j};
                }
            }
        }

        return new int[] {0};
    }
}