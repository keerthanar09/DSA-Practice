//Leetcode-75: Program to reverse the vowels in a string, keeping the remaining string in the same order.

public class ReverseVowel {
    public static void main(String [] args) {
        String s = "Ice CreAm";
        char [] word = s.toCharArray();
        int start = 0;
        int end = s.length()-1;
        String vowels = "aeiouAEIOU";
        char temp;
        while(start<end)
        {
            while(start<end && vowels.indexOf(word[start])==-1)
            {
                start++;
            }
            while(start<end && vowels.indexOf(word[end])==-1)
            {
                end --;
            }
            temp = word[start];
            word[start] = word[end];
            word[end] = temp;
            start++;
            end--;
        }
        String answer = new String(word);
        System.out.println("The reversed string is " + answer);
    }
}
