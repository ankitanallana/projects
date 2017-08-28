package Week2;

import java.util.ArrayList;
import java.util.List;

public class findDuplicates {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int[] nums = {4, 3, 2, 7, 8, 2, 3, 1};
		System.out.println(findDuplicates(nums));
	}
	public static List<Integer> findDuplicates(int[] nums) {
        List<Integer> result = new ArrayList<Integer>();
        int index = 0;
        /* index-1 handles ArrayIndexOutOfBounds */
        for(int i=0;i<nums.length;i++){
        	index = Math.abs(nums[i]) - 1;
        	if(nums[index]>0){
        		nums[index] = -nums[index];
        	}
        	else result.add(Math.abs(nums[i]));
        }
        
        
        return result;
    }
}
