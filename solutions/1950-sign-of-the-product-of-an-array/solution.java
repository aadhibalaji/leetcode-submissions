class Solution {
    public int arraySign(int[] nums) {
        int zeros = 0;
        int pos = 0;
        int neg = 0;
        for (int i = 0; i<nums.length; i++){
            if (nums[i]==0){
                zeros++;
            }
            else if (nums[i]>1){
                pos++;
            }
            else if (nums[i]<1){
                neg++;
            }
        }
       
        if (zeros>0){
            return 0;
        }
        else if (neg%2 == 0){
            return 1;
        }
        else {
            return -1;
        }
        
    }
}
