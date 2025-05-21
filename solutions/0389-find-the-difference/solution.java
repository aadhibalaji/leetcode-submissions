class Solution {
    public char findTheDifference(String s, String t) {
        char character;
        char output = ' ';
        boolean equal = false;
        char characterTwo;
        int counter = 0;
        int counterTwo = 0;
    
        for (int g = 0; g<t.length(); g++){
                character = t.charAt(g);
                for (int i = 0; i<s.length(); i++){
                    if (character==s.charAt(i)){
                        counter++;
                    }
                }
                for (int j = 0; j<t.length(); j++){
                    if (character==t.charAt(j)){
                        counterTwo++;
                    }
                }
                if (counter!=counterTwo){
                    output = character;
                }
                counter = 0;
                counterTwo = 0;
            }

        

        return output;
            
    }

}
        

    
        
       

