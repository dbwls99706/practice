#include <string>
#include <vector>

using namespace std;

int solution(int n) {
    int a = 1;
    while(1){
        if(n % a == 1){
            return a;
        }
        a++;
    }
}