class Solution {
    public int[] twoSum(int[] nums, int target) {
        ArrayList<Integer> results = new ArrayList<>();

        for (int i = 0; i < nums.length; i++) {
            for (int j = i + 1; j < nums.length; j++) {
                if (target == nums[i] + nums[j]) {
                                results.add(i);
                                results.add(j);
                }
            }
        }

        return results.stream().mapToInt(Integer::intValue).toArray();
    }
}