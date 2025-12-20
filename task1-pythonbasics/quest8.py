import sys

string = input('enter a string - ')

p=len(string)
strng = list(string)

n=input('enter a number')
n=int(n)
i=0

if p%n!=0:
    print('invalid input')
    sys.exit()
    

while i<p:
    for j in range(i,n):
        print(strng[j],end='')
        
    print('')
    i=i+n
    n=n+i
   

