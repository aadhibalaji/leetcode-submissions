class Solution {
    public int lengthOfLastWord(String s) {
        char letter = 'a';
        int length = 0;
        for (int i = s.length()-1; i>=0;i--){
            letter = s.charAt(i);
            if (letter!=' '){
                length++;
                if (i!=0){  
                    if (s.charAt(i-1)==' '){
                        break;
                    }

                }
            }
            
        }
        return length;
    }
}
