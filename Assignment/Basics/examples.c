/*Verify the limited precision of floats and double (e.g. try to compute 1/(a-b) where
a=1+epsilon and b =1-epsilon)*/

/*Good pratice with floating points:
Precision Loss:
    Use double over float when possible, as double has more precision.
    Be cautious of cumulative rounding errors in iterative calculations.

Comparisons:
    Avoid direct equality checks. Use a small tolerance value.
*/

/*Suppose you have some flags represented “bitmask” i.e. an integer where each bit represent some true/false value
○ take the value of bit number 7 to define a boolean variable called isValidData
○ print the value of “isValidData”*/

#include <stdio.h>
#include <stdbool.h>

void printBits(int u) { 
    /* Remember that binary representation has to be read from right to left!!*/
    printf("Binary representation: ");
    int totalBits = sizeof(u) * 8;

    for (int i = totalBits - 1; i >= 0; i--) {
        printf("%d", (u >> i) & 1);
        // Add a space after 8 bits (1 byte)
        if (i % 8 == 0 && i != 0) {
            printf(" ");
        }
    }
}

int main(){

    printf("First assignment\n");
    for(double epsilon=1e-9; epsilon>1e-20; epsilon/=10){

        float a=1; //float 1.00000000001=1.0
        float b=1;
        a=+epsilon;
        b=-epsilon;
    
        printf("epsilon: %.e\n", epsilon); //always remember to put the \n at the end of the printf
        printf("1/(a-b) %.f, mentre 1/2epsilon %.f\n", 1.f/(a-b), 1.f/(2.f*epsilon));
    }
    printf("\n\n");

    printf("Second assignment\n");
    int bitmask = 566;

    printBits(566);
    printf(" of %d\n ", bitmask); 


    // 1 << 7: This shifts the binary number 1 left by 7 positions
    printBits(1<<7); 
    printf(" of 1\n "); 

    /*
    The & operator performs a bitwise AND between bitmask and 0b10000000.

    This means it compares each bit of bitmask with the corresponding bit in 0b10000000.
    If the 7th element is not 1, then the all thing chrashes and the mask goes to False.
    */

    bool isValidData = (bitmask & (1 << 7)) != 0; //isValidData is a mask and a boolean variable itself

    printf("isValidData: %s\n", isValidData ? "true" : "false"); //remember that the operator ? indicates that 

    return 0;
}