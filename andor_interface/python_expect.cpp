#include <iostream>
#include <expect.h>
#include <unistd.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <fcntl.h>
using namespace std;
int ready(FILE *f)
{   enum HOST_STATE { READY,FAILED,ACTION};
    int cas = exp_fexpectl(f,exp_glob,"exposure time\? (in seconds):",ACTION,exp_glob,"Name of the object:",ACTION,exp_glob,"acq mode: \[Target, video, dark, flat]:",ACTION,exp_glob,">>>",READY,exp_glob,"exposure time\? (in seconds):",ACTION,exp_end);//,exp_glob,"0\n",SUCCESS,exp_glob,"-1\n",FAILED,exp_end);

    switch (cas) {
        case READY:
        {
            return 0;
        }

        case FAILED:
        {
            //exp_fexpectl(f,exp_glob,">>>",READY,exp_end);
            return -2;
        }
        case ACTION:
        {
            return 1;
        }
        default:
        {
            return -1;
        }

    }
}
int command(FILE *f,std::string cmd,char output[499])
{   size_t length;
    length = 500;
    char str[length]={};

    fprintf(f,cmd.c_str());
    int result = ready(f);
    cout<<result<<endl;
    if (result<0)
    {
        return result;
    }
    strcpy(str,exp_buffer);
    str[length-1]='\0';
    strcpy(output,str);
    output[500-1]='\0';
    char * token = strtok(str,"\n");
    char *last[2] = {};
    int i=0;

    while (token!=NULL)
    {
        last[i%2] = token;
        token = strtok(NULL,"\n");
        i++;
    }

    char answ[100] = {};

    strcmp(last[0],">>>")==0 ? strcpy(answ,last[1]) : strcpy(answ,last[0]);
    answ[99]='\0';
    int ANSW;
    sscanf(answ,"%d",&ANSW);

    return ANSW;
}

FILE* initF(char output[BUFSIZ])
{
    FILE *f = exp_popen((char *)"PYTHONPATH=/home/pesto/module/:/home/pesto/data_andor/python/ python");
    ready(f);
    strcpy(output,exp_buffer);
    output[BUFSIZ-1]='\0';

    return f;
}

void close_exp(void)
{
    exp_disconnect();
}
void command_bash(std::string cmd,char output[499])
{   FILE *f = exp_popen((char*)cmd.c_str());
    ready(f);
    strcpy(output,exp_buffer);
    output[BUFSIZ-1]='\0';

    return ;
}
