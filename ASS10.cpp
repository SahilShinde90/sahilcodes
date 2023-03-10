#include <iostream>
using namespace std;
#define size 10

class stack
{
    int top;
    char stk[size];
    public:
    stack()
    {
     top=-1;
    }
    void push(char);
    char pop();
    int isfull();
    int isempty();
};

void stack::push(char x)
{
    top=top+1;
    stk[top]=x;
}

char stack::pop()
{
    char s;
    s=stk[top];
    top=top-1;
    return s;
}

int stack::isfull()
{
    if(top==size)
        return 1;
    else
        return 0;
}

int stack::isempty()
{
    if(top==-1)
        return 1;
    else
        return 0;
}

int main()
{
    stack s1;
    char exp[20],ch;
    int i=0;
    cout<<"\nEnter the expression to check whether it is in well form or not: \n";
    cin>>exp;
    if((exp[0]==')')||(exp[0]==']')||(exp[0]=='}'))
    {
        cout<<"\n Invalid Expression.....\n";
        return 0;
    }
    else
    {
        while(exp[i]!='\0')
        {
            ch=exp[i];
            switch(ch)
            {
            case '(':s1.push(ch);break;
            case '[':s1.push(ch);break;
            case '{':s1.push(ch);break;
            case ')':s1.pop();break;
            case ']':s1.pop();break;
            case '}':s1.pop();break;
            }
            i=i+1;
        }
    }
    if(s1.isempty())
    {
        cout<<"\n\nExpression is well parenthesised\n";
    }
    else
    {
        cout<<"\n\nSorry !!! Invalid Expression or not in well parenthesized\n";
    }
    return 0;
}

