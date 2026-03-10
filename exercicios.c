#include <stdio.h>

int main() {
    int A = 1; 
    int B = 1; 
    int C = 1;  
    int D = 1; 
    
    if ((A && !B && !C) || D) {
        printf("ON\n");
    } else {
        printf("OFF\n");
    }
    
    return 0;
}