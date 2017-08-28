package Week1;

public class FindIslands {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		//int[][] friendships = {{1,1,0},{1,1,0},{0,0,1}};
		//int[][] friendships = {{1,1,0},{1,1,1},{0,1,1}};
		int[][] friendships = {{1,0,0,1},{0,1,1,0},{0,1,1,1},{1,0,1,1}};
		System.out.println(findCircleNum(friendships));
	}
	
	public static int findCircleNum(int[][] M) {
	        
		if(M.length<1){
			return 0;
		}
		else {
			if(M[0].length<1){
				return 0;
			}
			else{
				/*
				 * Calculate friend circles here 
				 * */
				int circles=0;
				for (int i=0;i<M.length;i++){
					for(int j=0;j<M[i].length;j++){
						if(M[i][j]==1){
							if(i+1<M.length)
							{dfs(M, i+1, j);}
							if(j+1<M[i].length)
							{dfs(M, i, j+1);}
							circles++;
							M[i][j] = 9;
							
						}
						
					}
				}
				return circles;
			}
			
		}
		
	    }
	public static void dfs(int[][] M, int i, int j){
		if(M[i][j]==0){
			return;
		}
		else {
			if(M[i][j]==1){
				if(i+1<M.length)
				{dfs(M, i+1, j);}
				if(j+1<M[i].length)
				{dfs(M, i, j+1);}
				M[i][j] = 9;
			}
		}
	}
}
