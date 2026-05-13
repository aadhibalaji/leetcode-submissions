class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> map = new HashMap<>();

        int[] result = new int[2];
        
        for (int j = 0; j < nums.length; j++) {
            int difference = target - nums[j];

            if(map.containsKey(difference)) {
                result[0] = map.get(difference);
                result[1] = j;
                break;
            }

            map.put(nums[j], j);
        }

        return result; 

    }
}
