// Collatz Problem
/*
    starting with number N

    next number : N/2 if N is even
                 3N+1 if N is odd
    
    numbers produce a chain to 1 

    the problem is which number under 1000000 produce the longest chain

*/

#include <stdio.h>
#include <iostream>

using namespace std;

int produceChain(uint a);

int main(){

    int start=1;
    int largest=0;
    int largestStart=0;

    while (start<1000000)
    {
        cout<<"processing... "<<start<<endl;
        int curr = produceChain(start);
        if (curr>largest)
        {
            largestStart = start;
            largest = curr;
        }
        start ++;    
    }
    cout << "the number that produces largest chain is " << largestStart <<" with chain length "<<largest<<endl;

    
    return 0;
}


int produceChain(uint a){

    int chainlength=0;
    do
    {
        if (a == 1)
        {
            break;
        }
        else if (a % 2 == 0)
        {
            a = a/2;
        }
        else
        {
            a = 3 * a +1;
        }

        chainlength ++;
    } while (a!=1);

    return chainlength; 
}


/* result:
    ..
    the number that produces largest chain is 837799 with chain length 524
*/