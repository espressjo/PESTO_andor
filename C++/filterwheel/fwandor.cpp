#include "fwandor.h"
#include "socket.h"
#include <string>
#include <algorithm>
using namespace std;
FW::FW()
{
FW::isHomed=0;//everytime the pesto is started the filter wheel is automatically not initialized
FW::adress = "132.204.61.142";// adress of the filter server at OMM

}
int FW::position(int pos)
{
    std::string cmd="1";
    std::string ANSW="-1";
    std::string WRITE="-1";
    std::string cmd2=std::to_string(pos);

    if (!FW::isHomed)
    {
        if (FW::home()==-1)
        {
            return -1;
        }
    }

    if (write_socket_address(8300,FW::adress,&cmd)==-1)
    {
        return -1;
    }
    if (write_socket_address(8301,FW::adress,&cmd2)==-1)
    {
        return -1;
    }
    if (write2way_adress(8400,FW::adress,WRITE,&ANSW)==-1)
    {
        return -1;
    }
    ANSW.erase(std::remove(ANSW.begin(), ANSW.end(), '\n'), ANSW.end());
    if (pos==stoi(ANSW))
    {
        return stoi(ANSW);
    }
    else
    {
        return -1;
    }


}

int FW::increment(void)
{   FW::isHomed=0;
    std::string cmd="1";
    std::string ANSW,WRITE="-1";
    std::string cmd2="+";

    write_socket_address(8300,FW::adress,&cmd);
    write_socket_address(8301,FW::adress,&cmd2);
    write2way_adress(8400,FW::adress,WRITE,&ANSW);
    ANSW.erase(std::remove(ANSW.begin(), ANSW.end(), '\n'), ANSW.end());
    //cout<<ANSW<<endl;
    return stoi(ANSW);
}
int FW::get_position(void)
{
    std::string cmd="1";
    std::string cmd2="?";
    std::string ANSW,WRITE="-1";
    write_socket_address(8300,FW::adress,&cmd);
    write_socket_address(8301,FW::adress,&cmd2);
    write2way_adress(8400,FW::adress,WRITE,&ANSW);
    ANSW.erase(std::remove(ANSW.begin(), ANSW.end(), '\n'), ANSW.end());
    //cout<<ANSW<<endl;
    return stoi(ANSW);
}

int FW::home(void)
{
    std::string cmd="1";
    std::string ANSW="-1";
    std::string WRITE="-1";
    std::string cmd2="H";


    if (write_socket_address(8300,FW::adress,&cmd)==-1){

        return -1;
    }
    if (write_socket_address(8301,FW::adress,&cmd2)==-1)
    {
        return -1;
    }
    if (write2way_adress(8400,FW::adress,WRITE,&ANSW)==-1)
    {
        return -1;
    }

    ANSW.erase(std::remove(ANSW.begin(), ANSW.end(), '\n'), ANSW.end());
    if (stoi(ANSW)==0)
    {
        FW::isHomed=1;
    }
    else {
        return -1;
    }
    return stoi(ANSW);
}
int FW::connection(std::string device)
{   FW::isHomed=0;
    std::string cmd="4";
    std::string ANSW,WRITE="-1";

    write_socket_address(8300,FW::adress,&cmd);
    write_socket_address(8301,FW::adress,&device);
    write2way_adress(8400,FW::adress,WRITE,&ANSW);
    ANSW.erase(std::remove(ANSW.begin(), ANSW.end(), '\n'), ANSW.end());
    return stoi(ANSW);

}
int FW::closeConnection(void)
{   FW::isHomed=0;
    std::string cmd="3";
    std::string ANSW,WRITE="-1";
    write_socket_address(8300,FW::adress,&cmd);
    write2way_adress(8400,FW::adress,WRITE,&ANSW);
    ANSW.erase(std::remove(ANSW.begin(), ANSW.end(), '\n'), ANSW.end());
    //cout<<ANSW<<endl;
    return stoi(ANSW);
}
