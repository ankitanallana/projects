package Week1;

import java.util.ArrayList;

public class FindFriendCircles {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		//int[][] friendships = {{1,1,0},{1,1,0},{0,0,1}};
		int[][] friendships = {{1,1,0},{1,1,1},{0,1,1}};
		//int[][] friendships = {{1,0,0,1},{0,1,1,0},{0,1,1,1},{1,0,1,1}};
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
				ArrayList<Integer> toVisit = new ArrayList<Integer>();
				ArrayList<ArrayList<Integer>> groups = new ArrayList<ArrayList<Integer>>();
				for (int i=0;i<M.length;i++){
					toVisit.add(i);
				}
				for (int i=0;i<M.length;i++){
					ArrayList<Integer> group = new ArrayList<Integer>();
					group.add(i);
					if(toVisit.contains(i)){
						toVisit.remove((Integer)i);
						for(int j=0;j<M[i].length;j++){
							if(i!=j){
								if(M[i][j]==1)
								{
									addAllFriends(group, j, M[i].length, M, toVisit);
									
								}
							}
						}
						groups.add(group);
					}
					
				}
				return groups.size();
			}

		}

	}
	
	public static void addAllFriends(ArrayList<Integer> group, int j, int n, int[][] M, ArrayList<Integer> toVisit ){
		group.add(j);
		toVisit.remove((Integer)j);
		for(int k = 0; k<n; k++){
			if(M[j][k]==1){
				if(toVisit.contains(k))
				{
					addAllFriends(group, k, n, M, toVisit);
				}
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
