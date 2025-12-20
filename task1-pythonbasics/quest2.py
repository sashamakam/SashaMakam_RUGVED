string = input('enter a string - ')
string_lower = string.lower()

char_list = list(string_lower)
print(char_list)

dict_count = {}

for c in char_list:
    if c in dict_count:
        dict_count[c]+=1
    else:
        dict_count[c]=1

print(dict_count)




i=0

while i < len(string):
    for j in range(0, len(string)-i-1):
        if char_list[j] > char_list[j+1]:
            temp = char_list[j]
            char_list[j] = char_list[j+1]
            char_list[j+1] = temp
    i+=1
    


print(''.join(char_list))


 
