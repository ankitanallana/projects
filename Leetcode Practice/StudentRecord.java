package Week2;

public class StudentRecord {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		System.out.println(checkRecord("LLLL"));
	}
	public static boolean checkRecord(String s) {
        int a = 0, l = 0;
        
        for (int i=0; i<s.length();i++){
        	if(s.charAt(i)=='A'){
        		a++;
        	}
        	
        	if(a>1){
        		return false;
        	}
        	
        	if(s.charAt(i)=='L'){
        		if(i==0){
        			continue;
        		}
        		if(s.charAt(i-1)=='L')
        			l++;
        		else l=0;
        	}
        	
        	if(l>1){
        		return false;
        	}
        }
        
        return true;
    }
}
