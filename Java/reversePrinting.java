/*
Write a program called Dec2Hex that prompts user for a positive decimal number, 
read as int, and print its equivalent hexadecimal string. 
The output shall look like:

Enter a decimal number: 1234
The equivalent hexadecimal number is 4D2
*/

import java.util.Scanner;

public class Dec2Hex {
    public static void main(String[] args) {
        final String[] HEX_CHAR = {
            "0", "1", "2", "3", 
            "4", "5", "6", "7",
            "8", "9", "A", "B",
            "C", "D", "E", "F",
        };

        Scanner input = new Scanner(System.in);
        System.out.print("Enter a decimal number: ");
        int num = input.nextInt();

        String result = "";

        while (num != 0) {
            int index = num % 16;
            result = HEX_CHAR[index] + result;
            num /= 16;
        }     
        System.out.println("The equivalent hexadecimal number is " + result);
    }
}