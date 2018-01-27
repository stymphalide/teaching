#include<stdio.h>

/*
int factorial(int n)
{
    if (n == 0)
    {
        return 1;
    } 
    else
    {
        return n * factorial(n-1);
    }
}
int factorial_for(int n)
{
    if (n == 0)
    {
        return 1;
    }
    int res = 1;
    for (int i = n; i > 0; --i)
    {
        res *= i;
    }
    return res;
}
*/

int main(int argc, char const *argv[])
{
    int n = 10;
    int res = 1;
    for (int i = n; i > 0; --i)
    {
        res *= i;
    }
    return res;
}