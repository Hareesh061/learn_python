# recursion in python


def fact(num):
    if(num ==0 or num==1):
        return 1
    else:
        return num*fact(num-1)

num = int(input("enter your number"))
print("your number fact is :", fact(num))




def fibo(n):
    if(n<=1):

        return n
    else:
    
        return (fibo(n-1)+fibo(n-2))

n = int(input())
print(fibo(n))



# fibonacci series 


n = int(input("enter number:"))
a=0
b=1
next=0

while(next<n):
    print(next)
    a=b
    b=next
    next=a+b
