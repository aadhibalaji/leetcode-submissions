class Solution {
    public boolean repeatedSubstringPattern(String s) {
        String copy = s;
        boolean output = false;
        int length = s.length();
        String sample = "";
        String test = "";
        int increment = 0; 

        for (int i = 1; i<length; i++){
            sample = s.substring(0, i);
            increment = length/i;
            test = "";
            for (int j = 0; j<increment; j++){
                test+=sample;
            }
            if (test.equals(s)){
                output = true;
                break;
            }
        }
        

        return output;
    }
}
