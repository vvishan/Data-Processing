# def star(n):
#     length = n*2 -1
#     star = 1
#     for i in range(1, n+1):
#         print(("*"* star).center(length) )
#         star += 2


# star(6)

# nums =[2,7,6,3,9]
# def longcosecut(n):
#     numset = set(n)
#     long =0

#     for i in numset:
#         if (i-1) not in numset:
#             length = 1
#             while (i+ length) in numset:
#                 length += 1
#                 long = max(length , long)
#     print(long)

# longcosecut(nums)

# z=['A','D','B','E','F']
# x= list(sorted(z))
# print(x)


# #carfleet
# position = [20,40,8,10,8]
# target = 5
# speed = [1,3,1,4,3]

# pair =[(p,s) for p,s in zip(position,speed)]

# stak =[]
# for p ,s in sorted(pair):
#     time = (target -p)/s
#     print(time)
#     while stak and time >= stak[-1]:
#         stak.pop()
#         stak.append(time)

# print(stak)

# #decorator
# def my_deco(func):
#     def wrapper():
#         print("running {func.name}")
#         func()
#         print("complete")
#     return wrapper
# @my_deco
# def do_this():
#     print("doing this")
# @my_deco
# def do_that():
#     print("doing that")

# do_this()
# do_that()

# num = int(input("check for the perfect square:"))
# l =1 
# r= num
# while l <= r:
#     m = (l+r) // 2
#     m_sq = m * m

#     if num == m_sq:
#         print("yes it is")
#     elif m_sq < num:
#         l = m+1
#     else:
#         r = m-1
#         break

# from collections import Counter
# s="raat"
# r="car"
# ds ={}
# for x in s:
#     if x  in ds:
#         ds[x] += 1
#     else:
#         ds[x] =1
# dt= {}
# for y in r:
#     if y in dt:
#         dt[y] +=1
#     else:
#         dt[y] =1

# print(ds)
# print(dt)
# print(ds == dt)

# f=[3,2,1,1,2,4]
# def majorityelements(n):
#     count =0
#     cadid = None

#     for i in n:
#         if count == 0:
#             cadid = i

#     count +=1 if cadid == i else -1
#    print(count)

# majorityelements(f)


# s = [4,5,6,None,None]
# x= [2,3,4,5,6,None,8]
# if all(x):
#     print("locker was full")
# elif any(x):
#     print("some waht")

#prime
# for i in range(1,50):
#     if i % 2 == 0:
#         print(i)

# for i in range(1,50):
#     for j in range(2,i):
#         if i % j ==0:
#             break
#     else:
#         print(i)

# a = "aabbbcccddd"
# def countalfa(x):
#     x = input(str("inout str:"))
#     dict = {}
#     for i in x:
#         if i in dict:
#             dict[i] += 1
#         else:
#           dict[i]=1

#     result =[]

#     for k,n in dict.items():
#         result.append(k+str(n))
#     print(''.join(result))

#     #print(result)
#     return dict
# countalfa(a)
# r =[5,5,10]
# def change(x):
#     five , ten = 0,0
#     for i in x:
#         if i == 5:
#             five +=1
#         if i == 10:
#             ten += 1
#         print(five,ten)
#         changes = i -5
#         if changes == 5:
#             if five < 0:
#                 five -= 1
#             else:
#                 print(False)
#                 return False
# change(r)

#valid parnthesis
# s = ")()"
# def validparn(x):
#     stack = []
#     open_to_stack = {")":"(","}":"{","]":"["}
#     for c in s:
#         if c not in open_to_stack:
#             stack.append(c)
#             print(stack)
#             continue
#         if not stack or stack[-1] != map[c]:
#             return False
#         stack.pop()
#     return(len(stack)==0)

# validparn(s)

# my_set : set[str] ={'jio','jen'}
# my_set.discard('hari')
# print(my_set)

# *a,b,c =range(5)
# print(a)

# arr=[1,3,4,5,9]
# print(arr[1:])

# s = "07:05:45PM"
# print(s[2:-2])

# hel = [2,3,4,5,3,2]
# dict = {}
# for i in hel:
#         dict[i] = dict.get(i,0)+1

# print(dict.values())


# arr = [2,3,4],[5,6,7],[1,8,9]
# print(len(arr[0]))
# prim =0
# sec =0
# length = len(arr[0])
# for count in range(length):
#     prim += arr[count][count]
#     sec += arr[count][(length-count-1)]
# print(abs(prim-sec))
# print(sec)

# arr = [2,3,4,5,6]
# count = [0]*7
# for i in arr:
#     count[i] +=1
#     print(count)
# n=5
# mid = (n + 1) // 2 - 1 
# print(mid)

# print(1%2)

# s =[2,3,1,4]
# s.extend(s[3:])
# s.extend([5])
# print(s)

# x=[[0]]*3,[[0]]*3
# x[0][0]=32
# x[1][0]=22
# print(x)
import random

#n =[1,2,3,4,5,6]
# #k = len(n)
# #print(n)
# def add(s):
#     k= len(s)
#     for i in range(k):
#         for j in range(i+1,k):
#             if s[i]+s[j] == 7:
#                 print(s[i],s[j])

#     return print([i],[j])

# add(n)

# class carmaker:
#     def __init__(self,name,make):
#         self.name = name
#         self.make = make
       

#     def meilage(self,mile):
#         self.mile =mile
#     def display(self):
#         print(f"am {self.name} driving the car {self.make} for {self.mile} long")
#         p=[]
#         p.append(self.mile)
# m=carmaker("rajesh","kia")
# m.meilage("400")
# m.display()



# def isperfectsquare(num):
#     l =1
#     r =num

#     while l <= r:
#         m=(l+r) // 2
#         m_square = m * m
#         #print(m,m_square)

#         if num == m_square:
#             return True
#         elif m_square < num:
#             l=m+1
#         else:
#             r=m-1
#     return False
import math
from collections import Counter
# for i in range(1,100):
#     if isperfectsquare(i) == True:
#         print(f"its a perfect square: {i}")

# num=[1,2,3,3,3,4]
# def possible_split(n):
#     count = Counter(n)

#     for f in count.values():
#         if f > 2:
#             print("false")
#             return False
#     #print("true")
#     return True

# possible_split(num)



# stack =[]
# stack.append(1)
# stack.append(2)
# stack.append(3)
# stack.append(4)
# reverse_list =[]
# print(f"stac:{stack}")
# while stack:
#     reverse_list.append(stack.pop())
#     # if stack.pop() == 3:
#     #     print("captured")
# print(reverse_list)

# class Stack:
#     def __init__(self):
#         self.items = []

#     def push(self,item):
#         self.items.append(item)

#     def pop(self):
#         if not self.is_empty():
#             return self.items.pop()
#         else:
#             return "stack is empty"
#     def is_empty(self):
#         return len(self.items) == 0

#     def size(self):
#         return len(self.items)


# def reverse(str):
#     stack = Stack()
#     reverse_str = ""
#     for char in str:
#         stack.push(char)
#     while not stack.is_empty():
#         reverse_str += stack.pop()
#     print(reverse_str)

# s = "abcd"
# reverse(s)
# g=Stack()
# #g.push(3)
# #g.push(4)
# #g.push(5)
# print(g.items)
# print(g.is_empty())
# print(g.size())
# print(g.pop())


# def max_sum_subarray(arr,k):
#     if len(arr) < k:
#         return "invalid ,please check the array length"

#     window_sum = sum(arr[:k])
#     max_sum = window_sum

#     for i in range(len(arr)-k):
#         window_sum = window_sum - arr[i] + arr[i + 1]
#         print(window_sum,arr[i],arr[i + 1])
#         max_sum = max(window_sum,max_sum)
#         print(max_sum)


# ar=(2,3,4,5,6,7,8,1,3,6)
# aj =(2,3)
# k=2

# max_sum_subarray(aj,k)


# s= "ab"
# e ="abcdefgefhef"
# f="ef"


# def find_sequence_string(str,find):

#     window_length = len(find)
  
#     count = 0
#     for i in range (len(str)-1):
#         extract = (str[i]+str[i+1])
#         #print(extract)
#         if (find == extract):
#             #print(find,extract)
#             count += 1
#     return count
         

# print(find_sequence_string(e,f)) 

# a = ['e','f','b','m','r']
# b= ['h','h','l','q','t']
# print(a+b)
# def merge_sort_list(x,y):
#     return sorted(set(x+y))

# print(merge_sort_list(a,b))


# x =['www.welnge.com',
# 'www.google.com']
# for i in x:
#     print(i.removeprefix("www."))



class node:
    def __init__(self,data):
        self.data = data
        self.next = None
class linkedlist:
    def __init__(self):
        self.head = None
        self.next = None

    def countlink(self):
        temp = self.head
        count = 0
        while temp:
            count += 1
            temp = temp.next
        return print(count)

    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data, end=",")
            temp = temp.next
        print()
    def reverse_link(self):
        prev = None
        curr = self.head
        nex = None
        result = []

        while curr != None:
            result.append(curr.data)
            nex = curr.next
            curr.next = prev
            prev = curr
            curr = nex
        # print(curr.data)
        result1 = result[::-1]
        print(result1)
    def sublink(self):
        dummy = linkedlist()
        left = 2
        right = 4

        leftprev , curr = dummy , self.head
        for i in range(left-1):
            leftprev , curr = curr, self.next
        print(leftprev,curr)    
    def reverselink(self):
        fast = self.head
        slow = self.head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        prev = None
        while slow:
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp

        left, right = self.head , prev
        while right:
            if left.data != right.data:
                return False
            left = left.next
            right = right.next
        return True


    

    def middlelink(self):
        if not self.head:
            return None

        fast = self.head
        slow = self.head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        print(slow.data)

    def cyclelist(self):
        temp = self.head
        if not temp or not temp.next:
            return False
        slow = temp
        fast = temp.next

        while slow != fast:
            if not fast or not fast.next:
                print(False)
            slow = temp.next
            fast = fast.next.next
        print(True)

    def removelink(self,val):
        tem = self.head
        while tem.next:
            if tem.next.data == val:
                tem.next = tem.next.next
            else:
                tem = tem.next

    



V = linkedlist()
V.head = node(1)
node1=node("S")
node2=node("v")
node3=node("A")
node4=node("I")
node5=node("P")
node6=node("H")

V.head.next =node1
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6


V1 = linkedlist()
V1.head = node(6)
node1=node(1)
node2=node(5)
node3=node(2)
node4=node(4)
node5=node(3)

V1.head.next =node1
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
# V1.print_list()

list1 =[2,5,8]
list2 =[1,3,4,6]
def merge_sorted_lists(list1, list2):
    merged_list = []
    i=j=0
    while i < len(list1) and j < len(list2):
        if list1[i] <= list2[j]:
            merged_list.append(list1[i])
            i += 1
        else:
            merged_list.append(list2[j])
            j += 1
    merged_list.extend(list1[i:])
    merged_list.extend(list1[j:])
    print(merged_list)


##merge_sorted_lists(list1,list2)
#print(list1[0:])



# ### duplicate numbers ###
# n1 = {1,1,3,4,5,5,6,7}
# def containduplicate(num):
#     tem = set()
#     for n in num:
       
#         if n in tem:
#             print(n)
#             return True
#     tem.add(n)
#     return False

# s = [2,5,4]

# def missingnumber(nu):
#     x=0
#     n = len(nu)
#     for i in range(1,n+1):
#         x ^= i

#     for j in nu:
#         x ^= j
#     return x

# def oldmissingnum(A):
#     x = [A[i] + 1 for i in range (len(A)-1) if A[i+1] != A[i] + 1]
#     return x


# nums1 = [4, 3, 2, 7, 8, 2, 3, 1]
# c = missingnumber(s)
# #print(c)
# num1 =[1,2,1,2,0,1,0,2]
# def swapelements(nums):
#     low, mid, high = 0, 0, len(nums) - 1

#     while mid <= high:
#         if nums[mid] == 0:
#             nums[low], nums[mid] = nums[mid], nums[low]
#             #print(nums[low],nums[mid])
#             low += 1
#             mid += 1
#         elif nums[mid] == 1:
#             mid += 1
#         else:
#             nums[mid], nums[high] = nums[high], nums[mid]
#             print(nums[mid],nums[high])
#             high -= 1

# # swapelements(num1)         
# print(num1)
# #majority elemenents
# c= [1,3,2,1,3,1,2,1,1]
# def majorityelement(nums):
#     count ={}
#     for num in nums:
#         count[num]= count.get(num,0)+1
#     inter = len(nums)//2
#     for num,count in count.items():
#         if count > inter:
#             return num
# d= majorityelement(c)
# print(d)

# #way2
# def majorityelements2(num):
#     vote =0
#     cand =None
#     for nu in num:
#         if vote ==0:
#             cand = nu
#             vote = 1
#         elif cand ==nu:
#             vote += 1 
#         else:
#             vote -= 1

#     if num.count(cand) > len(num)//2:
#         return cand
#     else:
#         return None


# f= majorityelements2(c)
# print(f)

###################################
## two sum
x = [2,3,5,6,7,9]
target = 5
def twosum (num):
    n= len(num)
    for i in range(n-1):
        for j in range(i+1):
            if x[i]+x[j] == target:
                print(i,j)

#twosum(x)

# low time compexity
target1= 16
def twosum2(nums,target1):
    
    n= len(nums)
    x= nums
    count ={}
    left = 0
    right = n-1
    while left < right:
        sum = x[left] + x[right]
        if sum == target1:
            print(left,right)
        elif sum < target1:
            left += 1
        else:
            right -= 1
            
    
#twosum2(x,target1)

## three sum
nums = [-1,0,1,2,-1,-4]
def threesum(x):
    target =0
    count=[]
    x= sorted(x)
    print(x)
    n= len(x)
    for i in range(n-2):
        left = i + 1
        right = n-1
        while left < right:
            tsum = x[i] + x[left] + x[right]
            print( x[i], x[left] , x[right])
            print(tsum)
            if tsum == target:
                count.append([x[i], x[left],x[right]])
                left += 1
                right -= 1
                while left < right  and x[left] == x[left-1]:
                    left +=1
                while left < right and x[right] == x[right+1]:
                    right -= 1
            elif tsum < target:
                left +=1
            else:
                right -= 1
    return count

# z=threesum(nums)
# print(z)
#product of itself
# num =[1,2,3,4]
# res =[1]*(len(num))
# print(res[0])
# pre = 1
# for i in range(len(num)):
#     res[i]= pre
#     pre *= num[i]
# print(res)
# post=1
# for i in range(len(num)-1,-1,-1):
#     res[i] *= post
#     print(post)
#     post *= num[i]
# print(res) 

w =['neet','beet','late']
re =""
for s in w:
    re += str(len(w))+'#'+s
print(re)
x= re[2:4]
y = len(x)
print(x,y)

def decodestr(st):
   res = []
   i = 0
   while i < len(st):
        # Find the position of the next '#' delimiter
        j = st.find('#', i)
        if j == -1:
            raise ValueError("Invalid input: '#' delimiter not found.")

        # Extract the length prefix and convert to integer
        length_str = st[i:j]
        if not length_str.isdigit():
            raise ValueError(f"Invalid length value: '{length_str}' is not a number.")
        length = int(length_str)

        # Calculate the start and end indices of the actual string
        i = j + 1
        j = i + length
        if j > len(st):
            raise ValueError("Invalid input: String length exceeds available characters.")

        # Append the extracted string to the result list
        res.append(st[i:j])
        i = j
   return res

decodestr(re)