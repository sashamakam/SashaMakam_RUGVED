word_bank = ['listen', 'silent', 'enlist', 'inlets', 'google', 'apple']

word=input('Enter a word in the word list: ')
wordlist = list(word)
n=len(word)
flag=0

for i in range(0,n):
    for j in range(0,n-1):
        temp = wordlist[j]
        wordlist[j]=wordlist[j+1]
        wordlist[j+1]=temp

        for k in range(0,6):
            if word_bank[k] == ''.join(wordlist) and word_bank[k]!=word  :
                flag=1
                print(word_bank[k])
                break
        

if flag==1:
    print(' IT IS AN ANOGRAM')
else:
    print('IT IS NOT AN ANOGRAM')

