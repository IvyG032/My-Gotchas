/*
Write a program called Hex2Bin that prompts user for a hexadecimal string and print its equivalent binary string. 
The output shall look like:
Enter a Hexadecimal string: 1abc
The equivalent binary for hexadecimal "1abc" is: 0001 1010 1011 1100
*/
import java.util.Scanner;

public class Hex2Bin {
    public static void main(String[] args) {
            
        final String[] HEX_BITS = {"0000", "0001", "0010", "0011",
                            "0100", "0101", "0110", "0111",
                            "1000", "1001", "1010", "1011",
                            "1100", "1101", "1110", "1111"};
        
        Scanner input = new Scanner(System.in);
        System.out.println("Enter a Hexadecimal string: ");
        String hexString = input.next();

        System.out.print("The equivalent binary for hexadecimal \"" + hexString + "\" is: ");
        
        for (int i = 0; i < hexString.length(); i++) {
            // Get individual character from input
            char c = hexString.charAt(i);
            // Convert them into numbers
            int num = Character.digit(c, 16);
            // Use this number as index to look up the String array
            String converted = HEX_BITS[num];
            // Print the binary form

            System.out.print(converted + " ");
        }
    }
}