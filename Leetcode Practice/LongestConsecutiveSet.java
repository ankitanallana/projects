package Week2;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.Map;

public class LongestConsecutiveSet {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int[]  nums = {100, 4, 200, 1, 3, 2};
		int[] n = {-1, 1, 0};
		System.out.println(longestConsecutive(nums));
	}
	public static int longestConsecutive(int[] nums) {
        int len = 0;
        Map<Integer, Integer> numberMap = new HashMap<Integer, Integer>();
        for(int a : nums){
        	numberMap.put(a, a);
        }
        
        Map<Integer, ArrayList<Integer>> numList = new HashMap<Integer, ArrayList<Integer>>();
        
        for(int a:nums){
        	
        	if(numberMap.isEmpty()) break;
        	
        	int temp_a = a;
        	while(numberMap.get(a-1)!=null){
        		ArrayList<Integer> temp ;
        		
        		if(numList.get(temp_a)!=null){
        			temp = new ArrayList<Integer>(numList.get(temp_a));
        			temp.add(a-1);
        			numList.put(temp_a, temp);
        			numberMap.remove(a-1);
        			
        		}
        		else {
        			temp = new ArrayList<Integer>();
        			temp.add(a-1);
        			numList.put(temp_a, temp);
        			numberMap.remove(a-1);
        		}
        		a = a-1;
        	}
        
        	a = temp_a;
        	while(numberMap.get(a+1)!=null){
        		ArrayList<Integer> temp ;
        		if(numList.get(temp_a)!=null){
        			temp = numList.get(temp_a);
        			temp.add(a+1);
        			numList.put(temp_a, temp);
        			numberMap.remove(a+1);
        		}
        		else {
        			temp = new ArrayList<Integer>();
        			temp.add(a+1);
        			numList.put(temp_a, temp);
        			numberMap.remove(a+1);
        			}
        		a = a+1;
        	}
        	if(numList.get(temp_a)==null){
        		numList.put(temp_a, new ArrayList<Integer>());
        	}
        	numberMap.remove(temp_a);
        }

        for(int num : numList.keySet()){
        	if(numList.get(num).size()+1 > len){
        		len = numList.get(num).size()+1;
        	}
        }
        
        return len;
    }
	
}
