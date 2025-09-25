string=input('enter a string')

p=len(string)

string_list=list(string)
spaces=0
for i in range(0,p):
    if string_list[i]==' ':
        spaces=spaces+1

letters=p-spaces
print('letters= ',letters)

words=spaces+1

sentances=0

for q in range(0,p):
    if string_list[q]=='.' or string_list[q]=='!' or string_list[q]=='?':
        sentances=sentances+1
    else:
        sentances=sentances+0

print('words = ', words)
print('sentances = ', sentances)

l=(letters/words)*100
s=(sentances/words)*100

cli = 0.0588*l-(0.296*s) - 15.8

print('grade level is : ', cli)
