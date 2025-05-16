class Solution {
    public String mergeAlternately(String word1, String word2) {
        String output = "";
        if (word1.length()>word2.length()){
            for (int i = 0; i<word2.length(); i++){
            output+=word1.charAt(i);
            output+=word2.charAt(i);
            }
            for (int i = word2.length(); i<word1.length(); i++){
                output+=word1.charAt(i);
            }
        }
        else {
            for (int i = 0; i<word1.length(); i++){
            output+=word1.charAt(i);
            output+=word2.charAt(i);
            }
            for (int i = word1.length(); i<word2.length(); i++){
                output+=word2.charAt(i);
            }
        }
        return output;
    }
}
