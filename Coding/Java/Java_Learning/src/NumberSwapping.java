import java.util.Scanner;

class NumberSwapping
{
    public static void main (String[] args)
    {
        // Create a Scanner object to read input
        // This Java code snippet is a program that swaps the values of two numbers entered by the
        // user. Here is a breakdown of what each part of the code does:
        Scanner scanner = new Scanner(System.in); 
        System.out.println("Enter first number: ");
	    System.out.println("New file check");
        int num1 = scanner.nextInt(); // Read first number
        System.out.println("Enter second number: ");
        int num2 = scanner.nextInt(); // Read second number     
        System.out.println("Before Swapping: num1 = " + num1 + ", num2 = " + num2);
        // Swapping numbers using a temporary variable
            num1=num1+num2;
            num2 = num1-num2;
        
        num1 = num1-num2;
        System.out.println("After Swapping: num1 = " + num1 + ", num2 = " + num2);
        // Close the scanner
        scanner.close();
        ///// thanks!   
	//// good boss	
    /// vaibhav




    }
}
