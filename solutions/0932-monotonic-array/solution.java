class Solution {
    public boolean isMonotonic(int[] nums) {
        int decrease = 0;
        int increase = 0;
        for (int i = 0; i<nums.length-1; i++){
            if (nums[i]<nums[i+1]){
                increase++;
            }
            if (nums[i]>nums[i+1]){
                decrease++;
            }
        }
        if (increase==0 && decrease>=0){
            return true;
        }
        else if (decrease==0 && increase>=0){
            return true;
        }
        else {
            return false;
        }
    }
}
