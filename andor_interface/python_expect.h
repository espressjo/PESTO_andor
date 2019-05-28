#ifndef PYTHON_EXPECT_H
#define PYTHON_EXPECT_H

#include <iostream>
#include <stdlib.h>

int ready(FILE *f);
int command(FILE *f,std::string cmd,char output[BUFSIZ]);
FILE* initF(char output[BUFSIZ]);
int close_exp(void);
void command_bash(std::string cmd,char output[499]);
#endif // PYTHON_EXPECT_H
