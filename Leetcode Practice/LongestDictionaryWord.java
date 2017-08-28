package Week2;

import java.util.ArrayList;
import java.util.List;

public class LongestDictionaryWord {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		List<String> d = new ArrayList<String>();
		d.add("apple");
		d.add("ewaf");
		d.add("awefawfwaf");
		d.add("awef");
		d.add("awefe");
		d.add("ewafeffewafewf");
		
		String s = "aewfafwafjlwajflwajflwafj";
		System.out.println(findLongestWord(s, d));
	}
	
	public static String otherCorrectMethod(String s, List<String> d){

    String longest = "";
    for (String dictWord : d) {
        int i = 0;
        for (char c : s.toCharArray()) 
            if (i < dictWord.length() && c == dictWord.charAt(i)) i++;
        System.out.println("dictWord - "+dictWord);
        System.out.println("subseqlen - "+i);
        if (i == dictWord.length() && dictWord.length() >= longest.length()) 
            if (dictWord.length() > longest.length() || dictWord.compareTo(longest) < 0)
                longest = dictWord;
    }
    return longest;
}	
	
	public static String findLongestWord(String s, List<String> d) {
        
		//find longest subsequence with every string
		String longest = "";
		for(String word : d){
			int subseqlen = 0;
			
			if(word.length()>=longest.length()){
				//find subsequence length
				subseqlen = findSubsequenceLength(s, word);
				
			}
			
			
			if(subseqlen==word.length() && word.length()>= longest.length()){
				if(word.length()==longest.length()){
					if(word.compareTo(longest)<0){
						longest = word;
					}
				}
				
				if(word.length()> longest.length()){
					longest = word;
				}
			}
			 
			
		}
		
		return longest;
        
    }
	
	public static int findSubsequenceLength(String str, String word){
		
		int i = 0;
		
		for (char c : str.toCharArray()) 
            if (i < word.length() && c == word.charAt(i)) i++;
		
		return i;
	}

}
