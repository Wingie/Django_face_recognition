#include "opencv2/opencv.hpp"
#include <string>
#include <iostream>
#include <sstream>
using namespace cv;
using namespace std;
string s0 ("./img/file");

string convertInt(int number)
{
   stringstream ss;//create a stringstream
   ss << number;//add number to the stream
   return ss.str();//return a string with the contents of the stream
}

int main(int, char**)
{
    VideoCapture cap(0); // open the default camera
    if(!cap.isOpened())  // check if we succeeded
        return -1;

    int i = 0;
    Mat frame;
    namedWindow("screen",1);
    string t;
    for(;;)
    {
        
        cap >> frame; // get a new frame from camera
			
		t = convertInt(i);
		t = s0+t;
		t = t + ".png";
		cout<<t<<endl;
        imwrite(t, frame);
        imshow("edges", frame);
        i++;
        if(waitKey(30) >= 0) break;
    }
    // the camera will be deinitialized automatically in VideoCapture destructor
    return 0;
}
