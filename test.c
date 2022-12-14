#include<stdio.h>
#include<Python.h>

int main()
{
    Py_Initialize();
    PyRun_SimpleString("X = 'waleczna ' + 'Lady Astryda'");
}