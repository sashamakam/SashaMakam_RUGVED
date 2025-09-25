#code to find weather a number is a hill number or not

num=input('enter a number: ')

list_num = [int(n) for n in num]

largest=0

for i in range(0,len(list_num)):
    if list_num[i]>largest:
        largest = list_num[i]

p=list_num.index(largest)

flag=0

for k in range(0,p):
    if list_num[k]>=list_num[k+1]:
        flag=1

for k in range(p,len(list_num)-1):
    if list_num[k]<=list_num[k+1]:
        flag=1

if flag==0:
    print('it is a hill number')
else:
    print('it is not a hill number')
    
