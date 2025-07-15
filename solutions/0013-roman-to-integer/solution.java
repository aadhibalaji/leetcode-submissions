class Solution {
    public int romanToInt(String s) {
        int output = 0;
        String letter = "";
        String letter2 = "";
        for (int i = 0; i<s.length(); i++){
            letter = String.valueOf(s.charAt(i));
            if (i<s.length()-1){
                letter2 = String.valueOf(s.charAt(i+1));
            }
            switch(letter){
                case "M": output+=1000;
                break;
                
                case "D": output+=500;
                break;

                case "C": 
                    if (letter2.equals("D")){
                        output+=400;
                        i++;
                    }
                    else if (letter2.equals("M")){
                        output+=900;
                        i++;
                    }
                    else{
                        output+=100;
                    }
                break;
                
                case "L": output+=50;
                break;

                case "X": 
                    if (letter2.equals("L")){
                        output+=40;
                        i++;
                    }
                    else if (letter2.equals("C")){
                        output+=90;
                        i++;
                    }
                    else{
                        output+=10;
                    }
                break;

                case "V": output+=5;
                break;

                case "I": 
                    if (letter2.equals("V")){
                        output+=4;
                        i++;
                    }
                    else if (letter2.equals("X")){
                        output+=9;
                        i++;
                    }
                    else{
                        output+=1;
                    }
                break;



            }

        }


        return output;
    }
}
