import java.util.Scanner;

class NumberSwapping
{
    public static void main (String[] args)
    {
        // Create a Scanner object to read input
        Scanner scanner = new Scanner(System.in); 
        System.out.println("Enter first number: ");
        int num1 = scanner.nextInt(); // Read first number
        System.out.println("Enter second number: ");
        int num2 = scanner.nextInt(); // Read second number     
        System.out.println("Before Swapping: num1 = " + num1 + ", num2 = " + num2);
        // Swapping numbers using a temporary variable
        int temp = num1;
        num1 = num2;
        num2 = temp;
        System.out.println("After Swapping: num1 = " + num1 + ", num2 = " + num2);
        // Close the scanner
        scanner.close();    





    }
}