#include <string>
#include <vector>

using namespace std;

long long solution(int a, int b) {
    long long answer = 0;
    int i = min(a, b);
    int j = max(a, b);
    for(;i < j+1; i++){
        answer+=i;
    }
    return answer;
}