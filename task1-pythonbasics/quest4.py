def selection_sort(string):
    n=len(string)
    for i in range(0,n-1):
        min_index=i
        for j in range(i+1,n):
            if string[j]<string[min_index]:
                min_index=j
            j=j+1

        temp=string[i]
        string[i]=string[min_index]
        string[min_index]=temp
        i=i+1
    return string

strng=input('Enter a string: ')
list_strng=list(strng)
print(''.join(selection_sort(list_strng)))

        


   
