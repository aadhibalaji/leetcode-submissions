class Solution {
    public boolean canMakeArithmeticProgression(int[] arr) {
        
        Arrays.sort(arr);
        int difference = 0;
        int newDifference = 0;
        int counter = 0;
        for (int i = arr.length-1; i>=1; i--){
            newDifference = arr[i] - arr[i-1];
            if (newDifference!=difference){
                difference = newDifference;
                counter++;
            }
        }
        if (counter<=1){
            return true;
        }
        else {
            return false;
        }
    }
}
