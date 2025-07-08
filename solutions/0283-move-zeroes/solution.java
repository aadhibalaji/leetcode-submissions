class Solution {
    public void moveZeroes(int[] nums) {
       int zeroes = 0;
       for (int n = 0; n<nums.length;n++){
        if (nums[n]==0){
            zeroes++;
        }
       }
       int counter = 0;
       for (int i = nums.length - 1; i>=0 ; i--){
        
            if (counter==zeroes){
                break;
            }        
        
            if (nums[i]==0){
                counter++;
                int k = i;
                for (int j = 0; j < nums.length - (i+1); j++){
                    
                    int zero = nums[k];
                    int swap = nums[k+1];
                    nums[k] = swap;
                    nums[k+1] = zero;
                    k++;
                }
                k = 0;
                  
            
            }    
        }




    }  
}
