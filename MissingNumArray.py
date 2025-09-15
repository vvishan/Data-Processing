# finding the missing or disppear number in the array

x= [8,3,5,6,7,2]

def missing_num(num):
    n = len(num)
    num1 = set(num)
    result =[]

    for i in range(1,n+1):
        if i not in num1:
            result.append(i)
    print(result)

missing_num(x)