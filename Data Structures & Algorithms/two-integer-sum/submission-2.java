class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> map = new HashMap<>();
        int[] results = new int[2];

        for (int i = 0; i < nums.length; i++){
            int diff = target - nums[i];
            System.out.println(diff);
            Integer partner = map.get(diff);
            if (partner != null) {
                System.out.println(partner);
                System.out.println(i);
                results[0] = partner;
                results[1] = i;
                return results;
            } else {
                map.put(nums[i], i);
            }
        }


        return null;
    }
}
