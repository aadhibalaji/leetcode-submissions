class Solution {
    public int calPoints(String[] operations) {
        ArrayList<Integer> s = new ArrayList<>();
        int counter = 0;

        for (int i = 0; i<operations.length; i++){
            String character = operations[i];
            switch (character){
                case "C": s.remove(counter-1); 
                counter--;
                break;
                
                case "D": s.add(counter, 2*s.get(counter-1));
                counter++;
                break;

                case "+": s.add(counter, s.get(counter-2)+s.get(counter-1));
                counter++;
                break;

                default: s.add(counter,Integer.parseInt(operations[i]));
                counter++;
            }
            System.out.println(s);
        }
        int output = 0;
        for (int j = 0; j<s.size(); j++){
            output+=s.get(j);
        }
        
        return output;


    }
}
