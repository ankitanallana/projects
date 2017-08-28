package Week2;

public class ReverseWordsInAString {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		 System.out.println(reverseWords("    the sky is blue    dont you think so?    "));
	}
	public static String reverseWords(String str){
		
		String[] array = str.trim().split("\\s+");
		String result="";
		
		for(int i=array.length-1;i>=0; i--){
			result = result+" "+array[i];
		}
		System.out.println(result.trim());
		return result;
	}
}
