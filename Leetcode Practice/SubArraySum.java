package Week2;

public class SubArraySum {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		/*Re-do using HashMap*/
		int[] nums = {1, 1, 1};
			//{5, 12, 7, 9, 6, 4, 15};
		System.out.println(subarraySum(nums, 3));
	}
	public static int subarraySum(int[] nums, int k) {
        int start = 0;
        int end = 0;
        int len = nums.length;
        
        int count = 0;
        
        int sum = 0;
        
        while(end<len){
        	sum = sum + nums[end];
        	
        	if(sum == k){
        		count++;
        		start = end;
        		end = start;
        		sum = 0;
        	}
        	
        	else if(sum>k){
        		sum = sum - nums[start];
        		start = start+1;
        		
        		if(sum==k){
            		count++;
            		start = end;
            		end = start;
            		
            	}
        		if(sum<k){
        			end = end+1;
        		}
        		if(start==end){
        			sum = 0;
        		}
        	}
        	else {
        		end = end+1;
        	}
        }
        		return count;
    }
}
