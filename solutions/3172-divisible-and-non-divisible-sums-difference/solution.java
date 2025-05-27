class Solution {
    public int differenceOfSums(int n, int m) {
        int num1 = 0;
        int num2 = 0;
        int remainder;
        for (int i = 1; i<=n; i++){
            remainder = i%m;
            if (remainder != 0){
                num1+=i;
            }
            else {
                num2+=i;
            }
        }
        return num1 - num2;
    }
}
