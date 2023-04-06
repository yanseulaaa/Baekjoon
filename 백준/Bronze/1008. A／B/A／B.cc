#include <stdio.h>

int main(){
    
    float A, B;
    
    scanf("%f %f", &A, &B);
    printf("%0.9lf",(double)A/B);
    
    return 0;
}