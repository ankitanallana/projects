package Week1;

public class ReshapeMatrix {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int[][] nums = {{1,2},{3,4}};
		int[][] matrix = matrixReshape(nums, 2, 2);
		printMatrix(matrix);
	}


    public static int[][] matrixReshape(int[][] nums, int r, int c) {
        int oldr=0;
        int oldc=0;
        if (nums.length!=0){
         oldr = nums.length;
            if(nums[0].length!=0){
                oldc = nums[0].length;
            }    
        }
        
        if(oldr*oldc != r*c){
            return nums;
        }
        else {
            /*reshape the matrix*/
            int[][] matrix = new int[r][c];
            int[] allElements = getAllElements(nums);
            matrix = fillUpElements(allElements, r, c);
            return matrix;
        }
    }
    
    public static int[] getAllElements(int[][] nums){
        int[] list = new int[nums.length*nums[0].length];
        int count = 0;
        for (int i = 0; i<nums.length; i++){
            for(int j=0;j<nums[i].length;j++){
                list[count] = nums[i][j];
                count++;
            }
        }
        return list;
    }
    
    public static int[][] fillUpElements(int[] list, int r, int c){
        int[][] matrix = new int[r][c];
        int count = 0;
        for (int i = 0; i<r; i++){
            for(int j=0;j<c;j++){
                matrix[i][j] = list[count];
                count++;
            }
        }
        return matrix;
    }
    
    public static void printMatrix(int[][] mat){
        
        for (int i = 0; i<mat.length; i++){
        	for(int j=0;j<mat[0].length;j++){
                System.out.print(mat[i][j]+"  ");
                }
        	System.out.println();
            
        }
        
    }

}
