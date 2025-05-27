#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

int solution(int n) {
    float answer = sqrt(n);
    if(answer == (int)answer){
        return 1;
    }
    else{
        return 2;
    }
}