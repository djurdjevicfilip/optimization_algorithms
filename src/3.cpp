#include <bits/stdc++.h>

using namespace std;


int cost_table[10][10] = {
    {0,374,200,223,108,178,252,285,240,356},
    {374,0,255,166,433,199,135,95,136,17},
    {200,255,0,128,277,821,180,160,131,247},
    {223,166,128,0,430,47,52,84,40,155},
    {108,433,277,430,0,453,478,344,389,423},
    {178,199,821,47,453,0,91,110,64,181},
    {252,135,180,52,478,91,0,114,83,117},
    {285,95,160,84,344,110,114,0,47,78},
    {240,136,131,40,389,64,83,47,0,118},
    {356,17,247,155,423,181,117,78,118,0},
};

class SpanningTree{
public:
    int *T, *V, *minArr, *G;
    unsigned int globalMin;
    int len;
    SpanningTree(int len){
        T = new int[2*(len+1)];
        this->len=len;
        V = new int[len+2]{};
        G = new int[len+2]{};
        minArr = new int[2*(len+1)];
        globalMin=-1;
    }

    
    // O(n2)
    void createFromSequence(int* P, int len){
        //Setup
        int q=0;
        int n=len+2;

        for (size_t i = 0; i < len; i++) P[i]++;
        for (size_t i = 0; i < n; i++) { V[i]=0; G[i]=0;}

        
        // Count the number of occurences for each number
        for (size_t i = 0; i < len; i++) V[P[i]-1]++;

        // Find the smallest element in V that does not appear in P
        for (size_t i = 0; i < len; i++)
        {
            for (size_t j = 0; j < n; j++)
            {
                // If element isn't in P
                if(V[j]==0){
                    V[j]=-1; // We've moved the element into V, so it's always going to be in V
                    
                    // Making the T array, where adjacent elements form an edge
                    T[q++] = j+1;
                    T[q++] = P[i];

                    V[P[i]-1]--; // Update after moving the element
                    break;
                }
            }
        }
            
        
        
        int j=0;

        // Connect the remaining 2 elements
        for (size_t i = 0; i < n; i++)
        {
            if(V[i] == 0 ){
                T[q++] = i+1;
                j++;
            } 
            if(j==2) break;
        }
        
        for (size_t i = 0; i < len; i++) P[i]--;

        // Count edges
        for (size_t i = 0; i < 2*(len+1); i++) G[T[i]-1]++;
        

        int currCost=calculateCost();

        if(currCost<globalMin){
            this->globalMin=currCost;
            fill(minArr);
        }
    }
    
    int calculateCost(){
        int cost=0;
        for (size_t i = 0; i < 2*(len+1)-1; i+=2)
        {
            cost += cost_table[T[i]-1][T[i+1]-1];
        }
        for (size_t i = 0; i < len+2; i++)
        {
            if(G[i]>=4) cost += 100*(G[i]-3);
        }
        
        return cost;
    }

    // Copy T to a
    void fill(int* a){
        for (size_t i = 0; i < 2*(len+1); i++)
        {
            a[i]=T[i];
        }
        
    }

    void printInfoWithMap(char* map){
        cout<<"Minimum cost: "<<this->globalMin<<endl;
        cout<<"Minimum spanning tree: ";
         for (size_t i = 0; i < 2*(len+1); i++)
        {
            cout << " " << map[minArr[i]];
            if((i+1)%2==0 && i<2*len) cout<<" - ";
        }
        cout<<endl;
    }

    friend ostream& operator<<(ostream& os, const SpanningTree& st){
        for (size_t i = 0; i < 2*(st.len+1); i++)
        {
            cout << " " << st.T[i];
            if((i+1)%2==0 && i<2*st.len) cout<<" - ";
        }

        cout<<endl;
        return os;
    }

    ~SpanningTree(){
        delete[] T;
        delete[] V;
        delete[] G;
        delete[] minArr;
    }
};




// Choosing k numbers from n - O(n^n-2)
void variationsWithRepetition(int n, int k, SpanningTree* st){
    int q;  //Current pointer (not a c++ pointer), starts from the end

    int* P = new int[k]{};


    do{
        st->createFromSequence(P, k);
        q=k-1; // Place at the end

        while(q >= 0){
            P[q]++;
            if(P[q] == n){
                P[q] = 0;
                q--;
            } else break;
        }
        

    }while(q >= 0);

    delete[] P;
}

int main(){
    int k=8, n=k+2;
    SpanningTree* st=new SpanningTree(k);

    char charMap[]={' ','A','B','C','D','E','F','G','H','I','J'};


    auto start = std::chrono::high_resolution_clock::now();
    variationsWithRepetition(n,k,st);

    auto finish = std::chrono::high_resolution_clock::now();
	cout<<"Measured performance: "<<std::chrono::duration_cast<std::chrono::milliseconds>( finish-start ).count()<<"ms"<<endl;
	
    st->printInfoWithMap(charMap);

    delete st;
    
}