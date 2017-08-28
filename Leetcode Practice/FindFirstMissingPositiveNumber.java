package Week1;

import java.util.HashMap;

public class FindFirstMissingPositiveNumber {
	

    public static int firstMissingPositive(int[] nums) {
        
        HashMap<Integer, Integer> map = new HashMap<Integer, Integer>();
        int max=Integer.MIN_VALUE;
        
        for(int i=0;i<nums.length;i++){
            if(nums[i]>0){
                map.put(nums[i], nums[i]);
                if (max<nums[i]){
                    max = nums[i];
                }
            }
        }
        
        
        for(int i=1;i<=max+1;i++){
            if(!map.containsKey(i)){
                return i;
            }
        }
        
        return 1;
    }


	public static void main(String[] args) {
		
		/* LeetCode accepted solution */
		
		int[] nums = {3,4,-1,1};
		System.out.println(firstMissingPositive(nums));
		
	}

}
