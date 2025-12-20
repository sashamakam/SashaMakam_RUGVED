def triple_and(a, b, c):
    return a and b and c
    
data1_str = (input("enter true or false: "))
data2_str = (input("enter true or false: "))
data3_str = (input("enter true or false: "))

data1 = (data1_str.lower()=='true')
data2 = (data2_str.lower()=='true')
data3 = (data3_str.lower()=='true')



print('\nYour result is: ')
print(triple_and(data1, data2, data3))




