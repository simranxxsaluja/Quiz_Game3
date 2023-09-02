public class Main
{
 public static void main(String[] args)
 {
 /* Declare and initialize variables for the following: number of friends, number of cookies, and total cost. Give these variables appropriate names and datatypes. */

    int numberOfFriends = 4;
    int numberOfCookies = 11;
    double cost = 6.00;
 
 /* Using your previously defined variables, calculate how much each person pays. Make a new variable of appropriate type and name and assign it to this value. */
 
    double individualPayment = numberOfCookies/cost;
 
 /* Using your previously defined variables, calculate how many whole cookies each person gets when cookies are split equally. Make a new variable of an appropriate type and assign it this value. */
 
    int individualCookies = numberOfCookies/numberOfFriends;
 
 /* Using only your first three variables, calculate how many cookies are left over. Make a new variable of an appropriate type and assign it this value. */
 
    int numberOfLeftoverCookies = numberOfCookies%numberOfFriends;
 
 
 /* Cast the variable representing how much each person pays to an int. Name the new object intPay. */

    int pay = individualPayment;
 }
}
