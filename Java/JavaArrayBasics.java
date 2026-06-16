/*
Write a program called PrintArray which prompts user for the number of items in an array (a non-negative integer), 
and saves it in an int variable called NUM_ITEMS. 
It then prompts user for the values of all the items and saves them in an int array called items. 
The program shall then print the contents of the array in the form of [x1, x2, ..., xn]. For example,

Enter the number of items: 5
Enter the value of all items (separated by space): 3 2 5 6 9
The values are: [3, 2, 5, 6, 9]
*/
import java.util.Scanner;

public class PrintArray {
    public static void main(String[] args) {
      // Declare variables
      final int NUM_ITEMS;
      int[] items;  // Declare array name, to be allocated after NUM_ITEMS is known
   
      // Prompt for for the number of items and read the input as "int"
      Scanner input = new Scanner(System.in);
      System.out.print("Enter the number of items: ");
      NUM_ITEMS = input.nextInt();
      // Allocate the array
      items = new int[NUM_ITEMS];

      // Prompt and read the items into the "int" array, if array length > 0

      if (items.length > 0) {
         System.out.print("Enter the value of all items (separated by space): ");
         for (int i = 0; i < items.length; ++i) {  // Read all items
            items[i] = input.nextInt();
         }
      }

      // Print array contents, need to handle first item and subsequent items differently
      System.out.print("The values are: ");
      for (int i = 0; i < items.length; ++i) {
         if (i == 0) {
            // Print the first item without a leading commas
            System.out.print(items[i]);
         } else {
            // Print the subsequent items with a leading commas
            System.out.print("," + items[i]);
         }
         // or, using a one liner
         //System.out.print((i == 0) ? ...... : ......);
      }

    }
}