package Week2;

public class IslandPerimeter {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int[][] grid={{0,1,0,0},{1,1,1,0},{0,1,0,0},{1,1,0,0}};
		System.out.println(islandPerimeter(grid));
	}
	public static int islandPerimeter(int[][] grid) {
        int count = 0;
		for(int i=0;i<grid.length;i++){
			for(int j=0;j<grid[i].length;j++){
				if(grid[i][j]==1){
					count = dfs(i, j, grid, count);
				}
			}
		}
		
		return count;
    }
	
	public static int dfs(int i, int j, int[][] grid, int count){
		
			
		if(i!=0 && grid[i-1][j]==0){
			count++;
			grid[i-1][j]=9;
		}
		else if(i!=0 && grid[i-1][j]==1){
			grid[i][j]=8;
			count = dfs(i-1, j, grid, count);
		}
		
		if(i!=grid.length-1 && grid[i+1][j]==0){
			count++;
			grid[i+1][j]=9;
		}
		else if(i!=grid.length-1 && grid[i+1][j]==1){
			grid[i][j]=8;
			count = dfs(i+1, j, grid, count);
		}
		
		if(j!=grid[i].length-1 && grid[i][j+1]==0){
			count++;
			grid[i][j+1]=9;
		}else if(j!=grid[i].length-1 &&grid[i][j+1]==1){
			grid[i][j]=8;
			count = dfs(i, j+1, grid, count);
		}
		
		if(j!=0 && grid[i][j-1]==0){
			count++;
			grid[i][j-1]=9;
		}else if(j!=0 && grid[i][j-1]==1){
			grid[i][j]=8;
			count = dfs(i, j-1, grid, count);
		}
		grid[i][j]=8;
		return count;
	}
}
