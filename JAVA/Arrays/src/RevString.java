//Leetcode 75 - Reverse the words in an input string (Medium).
import java.util.*;
public class RevString {
    public static void main(String [] args) {

        String s = "the sky is blue";
        String ns = s.trim().replaceAll("\\s+", " ");
        String [] words = ns.split(" ");
        List <String> rev = new ArrayList <String>();
        for(int i = words.length-1; i>=0; i--)
        {
            rev.add(words[i]);
        }
        System.out.println(String.join(" ", rev));
    }
}

