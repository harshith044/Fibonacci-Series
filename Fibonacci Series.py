def fib(n):
    number=0;
    a=0;
    b=1;
    temp=0;
    while number<=n:
        print(a);
        temp=a+b
        a=b
        b=temp
        number=number+1
fib(12)
