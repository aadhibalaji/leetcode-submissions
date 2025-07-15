class Solution {
    public int[] plusOne(int[] digits) {
        int counter =0;
        int[] finalDigitsOne = new int[digits.length];
        int[] finalDigitsTwo = new int[digits.length+1];
        if (digits[digits.length-1]!=9){
            digits[digits.length-1] = digits[digits.length-1] +1;
            for (int j = 0; j<digits.length; j++){
                finalDigitsOne[j] = digits[j];
            }
        }
        else if(digits[digits.length-1]==9){
            int carry = 1;
            for (int i = digits.length-1; i>=0; i--){
                if (carry==0){
                    break;
                }
                if (i==0 && digits[i]==9){
                    digits[i] = 1;
                    counter++;
                    break;
                }
                else if (i==0 && digits[i]!=9){
                    digits[i] = digits[i] + 1;
                    break;
                }
                

                if (digits[i]+carry==10){
                    carry = 1;
                    digits[i] = 0;
                }
                else if (digits[i]+carry!=10){
                    
                    digits[i]+=carry;
                    carry = 0;
                }
                
                
            }
            if (counter>0){
                for (int j = 0; j<digits.length; j++){
                    finalDigitsTwo[j] = digits[j];
                }
                finalDigitsTwo[digits.length] = 0;
                
            }
            else {
                for (int j = 0; j<digits.length; j++){
                    finalDigitsOne[j] = digits[j];
                }
            }
           

        }
        if (counter>0){
            return finalDigitsTwo;
        }
        else {
            return finalDigitsOne;
        }
       
    }
}
