package Week2;

public class MedianOfTwoSortedArrays {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
	}
	public static double findMedianSortedArrays(int[] nums1, int[] nums2) {
		
		int mhigh = nums1.length;
		int nhigh = nums2.length;
		int sumLen = mhigh+nhigh;
		
		if(sumLen % 2 == 0){
			return findKthSmallest(nums1, mhigh, 0, nums2, nhigh, 0, sumLen / 2 + 1);
		}
		else return (findKthSmallest(nums1, mhigh, 0, nums2, nhigh, 0, sumLen / 2)
				+ findKthSmallest(nums1, mhigh, 0, nums2, nhigh, 0, sumLen / 2 + 1)) / 2.0;
	}

	public static double findKthSmallest(int[] a, int m, int begin1, int[] b, int n, int begin2, int k){
		
		if(m>n){
			return findKthSmallest(b, n, begin2, a, m, begin1, k);
		}
		
		if(m==0){
			return b[begin2+k-1];
		}
		if (k == 1){
			return Math.min(a[begin1], b[begin2]);
		}
		
		int limitA = Math.min(k/2, m), limitB = k - limitA;
		
		//check if medians are equal
		if(a[begin1 + limitA - 1] == b[begin2 + limitB - 1]){
			return a[begin1 + limitA - 1];
		}
	
		else if (a[begin1 + limitA - 1] > b[begin2 + limitB - 1]){
			return findKthSmallest(a, m, begin1, b, n - limitB, begin2, k - limitB);
		}
		else return findKthSmallest(a, m - limitA, begin1 + limitA, b, n, begin2, k - limitA);
	}
}
