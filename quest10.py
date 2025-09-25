credit = input('enter your credit card number')

crdt = [int(i) for i in credit]
n=len(crdt)

i=n-2


while i>=0:
    # crdt[i]=int(crdt[i])
    crdt[i]=crdt[i]*2
    if crdt[i]>9:
        crdt[i]=crdt[i]-9
    i=i-2

print(crdt)

total=sum(crdt)

if total % 10 == 0:
    print('it is a credit card number')
else:
    print('it is not a credit card number')