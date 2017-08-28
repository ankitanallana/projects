package Week2;

public class NumberToWords {
	//TOO LONG AND TEDIOUS - TOO FORMULAIC
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		numberToWords(546);
	}
	public static String numberToWords(int num) {
        String words="";
        
        int digits = getNumberOfDigits(num);
        System.out.println("digits - "+digits);
        int groups = digits/3 + 1;
        
        int[] allDigits = convertToIntegerArray(num, digits);
        //System.out.println(allDigits[0]);
        
        for(int i = 0; i<allDigits.length ; i=+3){
        	String groupName = "";
        	System.out.println("i - "+allDigits[i]);
        	System.out.println("i+1 - "+allDigits[i+1]);
        	System.out.println("i+2 - "+allDigits[i+2]);
        	
        	
        	
        }
        
        
        return "huh";
    }
	
	public static int getNumberOfDigits(int num){
		int n = 0;
		while(num>0){
			num = num/10;
			n++;
		}
		return n;
		
		}
	
	public static int[] convertToIntegerArray(int num, int digits){
		
		int[] array = new int[digits];
		int remainder = 0;
		int counter = digits-1;
		while(num>0){
			remainder = num % 10;
			array[counter] = remainder;
			counter--;
			num = num/10;
		}
		
		return array;
		}
	
}
