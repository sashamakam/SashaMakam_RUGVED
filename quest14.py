def first_repeating(arr):
    n=len(arr)
    for i in range(0,n):
        for j in range(i,n):
            if arr[i]==arr[j]:
                return arr[j]
            
array=[1,5,8,4,6,1,6,3,9,10]
print('the first repeating element is ', first_repeating(array))