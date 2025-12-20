n=input('enter a number')
n=int(n)

for i in range(0,n+1):
    for j in range (0,n-i):
        print(' ',end='')
    for j in range(0,i):
        print('* ',end='')
    print('\n')

for i in range(n,0,-1):
    for j in range (0,n-i):
        print(' ',end='')
    for j in range(0,i):
        print('* ',end='')
    print('\n')

for i in range(0,n):
    for j in range(0,i):
        print('* ',end='')
    for j in range(2*(n-i)):
        print(' ',end='')
    for j in range(0,i):
        print('* ',end='')
    print('\n')

for i in range(0,2*n-1):
    print('* ',end='')

for i in range(n,0,-1):
    for j in range(0,i):
        print('* ',end='')
    for j in range(2*(n-i)):
        print(' ',end='')
    for j in range(0,i):
        print('* ',end='')
    print('\n')

