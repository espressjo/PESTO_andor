#include <iostream>
#include "fwandor.h"
#include <cstdlib>
using namespace std;

int main(int argc, char** argv)
{
    FW fw;
    if (argc!=2)
    {
        cout<<"Usage: fwandor <position>"<<endl;
        cout<<"-1"<<endl;
        return -1;
    }
    int filter = stoi(argv[1]);
    if (filter< 0 || filter>5)
    {
        cout<<"position must be between 0 and 5 inclusively"<<endl;
        cout<<"-1"<<endl;
        return -1;
    }
    int error = 0;
    if (filter==0)
    {
        error = fw.home();
    }
    else
    {
        error = fw.position(filter);
    }

    if (error!=filter)
    {
        cout<<"-1"<<endl;
        return -1;
    }
    else {
        cout<<"0"<<endl;
    }
    return 0;
}
