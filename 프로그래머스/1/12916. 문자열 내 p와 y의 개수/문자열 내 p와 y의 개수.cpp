#include <string>
#include <iostream>
using namespace std;

bool solution(string s)
{
    bool answer = true;
    int a = 0;
    int b = 0;
    for(int i=0;i < s.size();i++){
        if(s[i]=='p' or s[i] == 'P'){
            a++;
        }
        else if(s[i]=='y' or s[i] == 'Y'){
            b++;
        }
    }
    return a==b;
}