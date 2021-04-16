#include <bits/stdc++.h>
using namespace std;

int main(){
    const int N=711;
    int cnt=0;
    
    // a) 

    auto start = std::chrono::high_resolution_clock::now();

    // Kod koji prolazi kroz sve kombinacije brojeva
    for (size_t x1 = 0; x1 <= N-3; ++x1)
        for (size_t x2 = x1+1; x2 <= N-2; ++x2)
            for (size_t x3 = x2+1; x3 <= N-1; ++x3)
                for (size_t x4 = x3+1; x4 <= N; ++x4){
                     if(x1+x2+x3+x4 == N && x1*x2*x3*x4 == N * pow(100,3)) {
                        cnt++;
                    }
                }

    cnt=0;
    auto finish = std::chrono::high_resolution_clock::now();
    
    cout<<std::chrono::duration_cast<std::chrono::milliseconds>( finish-start ).count()<<endl;
    
    // b)

    start = std::chrono::high_resolution_clock::now();

    // Kod koji prolazi kroz sve kombinacije brojeva
    for (size_t x1 = 0; x1 <= N-3; ++x1)
        for (size_t x2 = x1+1; x2 <= N-2; ++x2)
            for (size_t x3 = x2+1; x3 <= N-1; ++x3){
                size_t x4=N-x1-x2-x3;
                if(x1*x2*x3*x4 == N * pow(100,3) && x4>x3){
                    
                    cout<<x1/100.0<<" "<<x2/100.0<<" "<<x3/100.0<<" "<<x4/100.0<<endl;
                    cnt++;
                }
            }  

    finish = std::chrono::high_resolution_clock::now();
    cout<<std::chrono::duration_cast<std::chrono::milliseconds>( finish-start ).count()<<endl;
}
