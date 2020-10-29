#include <bits/stdc++.h>
using namespace std;
vector<int> v;

class Point{
  public:
    double x,y;
    int position;
    Point(double x, double y, int position) :x(x),y(y), position(position){}
    friend bool operator<( const Point& a, const Point& b ) { return a.position<b.position; }
   
};

double** initDistanceMatrix(vector<Point> myVect, int size){
   double** distanceMatrix=new double*[size+1];

    for (size_t i = 0; i < size+1; i++)
    {
      distanceMatrix[i]=new double[size+1];
      
    }
    
    for (size_t i = 0; i < size; i++){
      for (size_t j = 0; j < size; j++){
         distanceMatrix[myVect.at(i).position][myVect.at(j).position]=sqrt(pow(myVect.at(i).x-myVect.at(j).x,2)+pow(myVect.at(i).y-myVect.at(j).y,2));
      }
    }
    return distanceMatrix;
}
void deleteDistanceMatrix(double** matrix, int sz){
  for (size_t i = 0; i < sz; i++)
  {
    delete[] matrix[i];
  }
  delete[] matrix;
  
}
void findMinimum(int size){
    v.clear();

    cout<<"SIZE: "<<size<<endl;
    //Init vector
    vector<Point> myVect;
    myVect.push_back(Point(62.0, 58.4,1));
    myVect.push_back(Point(57.5, 56.0,2));
    myVect.push_back(Point(51.7, 56.0,3));
    myVect.push_back(Point(67.9,19.6,4));
    myVect.push_back(Point(57.7, 42.1,5));
    myVect.push_back(Point(54.2, 29.1,6));
    myVect.push_back(Point(46.0, 45.1,7));
    myVect.push_back(Point(34.7, 45.1,8));
    if(size==12){
      myVect.push_back(Point(45.7, 25.1,9));
      myVect.push_back(Point(34.7, 26.4,10));
      myVect.push_back(Point(28.4, 31.7,11));
      myVect.push_back(Point(33.4, 60.5,12));
    }
    double** distanceMatrix=initDistanceMatrix(myVect,size);
    double min=-1;
    
    auto start = std::chrono::high_resolution_clock::now();
    do {
      double localMin=0;
      for (size_t i = 0; i < size-1; i++)
      {
          localMin += distanceMatrix[myVect.at(i).position][myVect.at(i+1).position];
      }
      if(localMin<min||min==-1){
          min=localMin;
          v.clear();
        for (size_t i = 0; i < size; i++)
        {
          v.push_back(myVect.at(i).position);
        }
      }
  } while (next_permutation(myVect.begin(),myVect.end()));

    auto finish = std::chrono::high_resolution_clock::now();
    
	cout<<"Measured performance: "<<std::chrono::duration_cast<std::chrono::milliseconds>( finish-start ).count()<<"ms"<<endl;
	
    cout<<"Minimum distance: "<<min<<endl;
    cout<<"Minimum distance path: ";
    for (size_t i = 0; i < size; i++)
      {
        cout<<v.at(i)<<" ";
      }
      cout<<endl;

      //Delete Matrix
      deleteDistanceMatrix(distanceMatrix, size);

      cout<<endl;
}

int main(){

   findMinimum(8);

   findMinimum(12);
}