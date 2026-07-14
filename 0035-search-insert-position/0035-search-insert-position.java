class Solution {
    public int searchInsert(int[] nums, int target) {
        int index = 0;
        int length = nums.length;
        
        while (index < length) {
            if (target <= nums[index]) {
                return index;
            }
            index ++;
        }

        return length;
    }
}