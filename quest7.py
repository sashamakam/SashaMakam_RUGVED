n=input('till which number do you want the fibonacci sequence?')


n=int(n)
a=0
b=1
for i in range(1,n):
    c=a+b
    print(c)
    a=b
    b=c
    i=i+1






