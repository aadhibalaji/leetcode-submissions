class Solution {
    public boolean judgeCircle(String moves) {
       int vert = 0;
       int horz = 0;
       for (int i = 0; i<moves.length(); i++){
           String s = String.valueOf(moves.charAt(i));
           switch(s){
            case "U": vert++;
            break;
            case "D": vert--;
            break;
            case "L": horz--;
            break;
            case "R": horz++;
           }

       } 
       if (horz==0 && vert==0){
        return true;

       }
       else {
        return false;
       }
    }
}
