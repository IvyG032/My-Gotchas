/*
10.3  hasEight() (method)
Write a boolean method called hasEight(), which takes an int as input and returns true if 
the number contains the digit 8 (e.g., 18, 168, 1288). The signature of the method is as follows:

public static boolean hasEight(int number);
Write a program called MagicSum, which prompts user for integers (or -1 to end), and produce the sum 
of numbers containing the digit 8. Your program should use the above methods. A sample output of the program is as follows:

Enter a positive integer (or -1 to end): 1
Enter a positive integer (or -1 to end): 2
Enter a positive integer (or -1 to end): 3
Enter a positive integer (or -1 to end): 8
Enter a positive integer (or -1 to end): 88
Enter a positive integer (or -1 to end): -1
The magic sum is: 96
*/

import java.util.Scanner;

public class MagicSum {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        System.out.print("Enter a positive integer (or -1 to end): ");
        int magicSum = 0;
        int inputNum = input.nextInt();

        while (inputNum != -1) {
            if (hasEight(inputNum)){
                magicSum += inputNum;
            }
            System.out.print("Enter a positive integer (or -1 to end): ");
            inputNum = input.nextInt();  
        }
        System.out.print("The magic sum is: " + magicSum);
    }

    public static boolean hasEight(int number) {
        while (number != 0) {
            int mod = number % 10;
            if (mod == 8) {
                return true;
            }
            else {
                number /= 10; // Java division truncates toward zero
            }
        }
        return false;
    }



}