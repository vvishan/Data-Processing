# Number of elements smaller than the current elements

num = [0,1,1,2,2,3]

def findsmallerElements(x):
    result =[]
    bucket ={}

    for i in range(len(x)):
        if x[i] not in bucket:
            bucket[x[i]] = i
    print(bucket)

    for i in x:
        result.append(bucket[i])
    print(result)

findsmallerElements(num)