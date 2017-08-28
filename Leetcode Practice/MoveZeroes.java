package Week2;

public class MoveZeroes {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int[] nums = {2,1,0,2};
		
		moveZeroes(nums);
		System.out.println("Final array:");
		for(int a : nums){
			System.out.println(a);
		}
	}
	
	public static void moveZeroes(int[] nums) {
		
		int swap = getNextSwap(nums, 0);
		int counter = swap+1;
		
		if(swap==-1){
			return;
		}
		
		for (int i=counter;i<nums.length;i++){
			if(nums[i]!=0){
				//swap positions
				nums[swap] = nums[i];
				nums[i] = 0;
				swap = getNextSwap(nums, swap);
			}
		}
		
		
	}
	
	public static int getNextSwap(int[] nums, int start){
		int swap = -1;
		/* initialize swap pointer*/
		for (int i=start;i<nums.length;i++){
			if(nums[i]==0){
				swap = i;
				break;
			}
		}
		return swap;
	}
}
