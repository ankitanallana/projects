package Week2;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.PriorityQueue;

public class MinHeap {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int[] nums1 = {0};
		int[] nums2 = {1};
		merge(nums1, 0, nums2, 1);
	}
	
	@SuppressWarnings({ "unchecked", "rawtypes" })
	public static void merge(int[] nums1, int m, int[] nums2, int n) {
	PriorityQueue<Integer> minheap=new PriorityQueue<Integer>();
	int mcount = 0;
	int ncount = 0;
	for(int x:nums1){
		if(mcount<m)
			minheap.add(x);
		mcount++;
	}
	for(int x:nums2){
		if(ncount<n)
			minheap.add(x);
		ncount++;
	}

	nums1 = new int[m+n];
	int counter = 0;
	System.out.println(minheap.toString());
	while(!minheap.isEmpty()){
		nums1[counter] = minheap.remove();
		//System.out.println(nums1[counter]);
		counter++;
	}
	
	
	}
}
