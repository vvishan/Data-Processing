def containduplicates(val):
    seen = set()
    for num in val:
        if num in seen:
            return True
        seen.add(num)
    return False

def missingnumbers(num):
    x = [num[i]+1 for i in range(len(num)-1) if num[i+1] != num[i]+ 1]
    return x

def numberdisappear(num):
    n=len(num)
    num_set = set(num)
    result =[]
    for i in range(1,n+1):
        if i not in num_set:
            result.append(i)
    return result
nums1 = [4, 3, 2, 7, 8, 2, 3, 1]
x=numberdisappear(nums1)
print(x)
            
def twosum(nums,target):
   
    n= len(nums)
    nums = sorted(nums)
    left = 0
    right = n-1

    while left < right:
        tsum = nums[left]+ nums[right]
        if tsum == target:
            return [left,right]
        elif tsum < target:
            left += 1
        else:
            right -= 1 

def Tsum(num):
    n = len(num)
    result=[]
    target = 0
   
    x=sorted(num)
    for i in range(n-2):
        left = i + 1
        right = n-1
    while left<right:
        ts = x[i]+x[left]+x[right]
        if ts == target:
            result.append([num[i],num[left],num[right]])
        elif ts < target:
            left += 1
        else:
            right -= 1
    return result
 
 # finding weather two strings are anograms

str1 = "Listen"
str2 = "Silent"

str1 = list(str1.upper())
str2 = list(str2.upper())
str1.sort()
str2.sort()
print(str1 == str2)

# counting the letters,numbers, spaces in the string

str = "python is 1"
import re
numbers = re.sub("[^0-9]","",str)
letters = re.sub("[^a-zA-Z]","",str)
spaces = re.findall("[ \n]",str)
print(len(numbers),len(letters),len(spaces))

# counting special characters in the string

special = "!@#$%^&*()"
count = re.sub('[\w]+', '',special)
print(len(count))

# removing all white spacs in the string

strin ="C O D E"
spaces = re.compile(r'\s+')
result = re.sub(spaces,"",strin)
print(result)

#building pyramids in python

floors = 3
h = 2*floors-1
for i in range(1,2*floors,2):
    print('{:^{}}'.format('*'* i,h))

#ramdomizing the item of the list in python

from random import shuffle
p = ["python", "is", "easy"]
shuffle(p)
print(p)

#finding the largest element in the list

t =[4,6,8,12,20,15,9]
largest = t[0]
for i in t:
    if largest < i:
        largest = i
    print(largest)

