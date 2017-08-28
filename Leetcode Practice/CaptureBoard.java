package Week2;

public class CaptureBoard {
	static int vLen;
	static int hLen;
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		char[][] board = {{'X','X','X','X'},{'X','O','O','X'},{'X','X','O','X'},{'X','O','X','X'}};
		solve(board);
	}
	public static void solve(char[][] board) {
		
		 vLen = board.length;
		 hLen = 0;
		if (vLen>0){
			hLen = board[0].length;
		}
		
		if(hLen>2 && vLen>2){
			
			for(int i = 0;i<vLen;i++){
				for(int j = 0;j<hLen;j++){
					if(board[i][j]=='O'){
						capture(board, i, j);
					}
				}
			}
			
			
			for(int i = 0;i<vLen;i++){
				for(int j = 0;j<hLen;j++){
					if(board[i][j]=='*'){
						board[i][j]='X';
					}
				}
			}
		}
	}
	
	public static void capture(char[][] board, int row, int col){
		if(row<0 || row>=vLen-1 || col<0 || col>=hLen-1 || board[row][col]=='X' || board[row][col]=='*'){
			return;
		}
		if(board[row][col]=='O')
		board[row][col] = '*';
		
		if(row>1 && board[row-1][col] == 'O')
			capture(board,row-1, col);
		
		if(row<hLen-2 && board[row+1][col] == 'O')
			capture(board,row+1, col);
		
		if(col>1 && board[row][col-1] == 'O')
			capture(board,row, col-1);
		if(col<vLen-1 && board[row][col+1] == 'O')
			capture(board,row, col+1);
	}
}
