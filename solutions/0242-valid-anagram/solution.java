class Solution {
    public boolean isAnagram(String s, String t) {
       char [] sChars = s.toCharArray();
       char [] tChars = t.toCharArray();
       Arrays.sort(sChars);     
       Arrays.sort(tChars); 
       int counter = 0;
       boolean output = false;
       if (s.length()<t.length()){
        output = false;
       }
       else if (s.length()>t.length()){
        output = false;
       }
       else {
            for (int i = 0; i<s.length(); i++){
            if (sChars[i]==tChars[i]){
                counter++;
            }
            if (counter==s.length()){
                output = true;
            }
       }
       }

        return output;
    }
}
