package Week2;

public class MatrixSearch {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int[][] matrix = {
		                  {1,   3,  5,  7},
		                  {10, 11, 16, 20},
		                  {23, 30, 34, 50}
		                };
		int[] vec = {1, 4, 6, 8, 11, 20, 30};
		//System.out.println(binarySearch(vec, 11, 0, vec.length-1));
		System.out.println(searchMatrix(matrix, 30));
	}
	
	public static boolean searchMatrix(int[][] matrix, int target) {
		int row = 0;
		
		if(matrix.length==0){
			return false;
		}
		
		if(matrix.length>0){
			if(matrix[0].length==0){
				return false;
			}
		}
		
		/*find row*/
		for(int i=0;i<matrix.length;i++){
			if(matrix[i][0]>target){
				row = i-1;
				break;
			}
			if(matrix[i][0]==target){
				return true;
			}
			if(i==matrix.length-1){
				return binarySearch(matrix[i], target, 0, matrix[i].length-1);
			}
		}
		if(row<0){
			return false;
		}
		/*binary search within row*/
		
		boolean found = binarySearch(matrix[row], target, 0, matrix[row].length-1);
		
		return found;
        
    }
	
	public static boolean binarySearch(int[] row, int target, int start, int end){
		int low = 0;
		int high = row.length - 1;

		while(high >= low) {
			int middle = (low + high) / 2;
			if(row[middle] == target) {
				return true;
			}
			if(row[middle] < target) {
				low = middle + 1;
			}
			if(row[middle] > target) {
				high = middle - 1;
			}
		}
		return false;
	}
}
