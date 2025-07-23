import java.util.HashSet;

public class LongestSubString {
    public static void main(String [] args) {
        int i = 0;
        int maxlength = 0;
        String s = "abcabcabcabcr";
        //HashSet is a collection that uses Hash Tables for storage.
        HashSet<Character> ch = new HashSet<Character>();

        for(int j = 0; j<s.length() ;j++)
        {
            while (ch.contains(s.charAt(j)))
            {
                ch.remove(s.charAt(i));
                i++;
            }
            ch.add(s.charAt(j));
            maxlength = Math.max(maxlength, j-i+1);
        }
        System.out.println(maxlength);
    
    }
}
