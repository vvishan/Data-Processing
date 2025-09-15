
# number dispear in array:
c=[2,3,6,7]
nums1 = [4, 3, 2, 7, 8, 2, 3, 1]
def numdispear(nums):
  n=len(nums)
  num_set = set(nums)
  result =[]
  for i in range(1,n+1):
    if i not in num_set:
      result.append(i)
  return result
#x=numdispear(nums1)
#print(x)
 # missing numbers in array

c=[2,3,6,7]
def missingnum(num):
  x=[num[i]+1 for i in range(len(num)-1) if num[i+1] != num[i]+1]
  return x
s= missingnum(nums1)
#print(s)
 
## number of elements smaller than current element
x = [8,1,1,2,2,3]

def numelements(xnum):
  num = sorted(xnum)
  print(num)
  bucket ={}
  result =[]
  for i in range(len(num)):
    if num[i] not in bucket:
      bucket[num[i]] = i 
  print(bucket)
  for i in xnum:
    result.append(bucket[i])
  print(result)

# numelements(x)
# print(x[0])

### insert thae element in the given sorted array
x1 =[2,3,4,6,7,8]
def insertele(num,target):
  
  low = 0
  high = len(num)-1
  #print(high)
  while low < high:
    mid = (low + high)//2
    #print(num[mid])
    if num[mid] == target:
      return mid
    elif num[mid] > target:
      high = mid -1
      #print(high)
    else:
      low = mid + 1
  return low
t=5
#print(insertele(x1,t))

### number of island

grid =[["1","1","0","0","0","1"],
       ["0","0","0","1","0","0"],
       ["1","1","0","0","0","1"],
       ]
def numberislands(gr):
  if not gr:
    return 0
  row,col =len(gr),len(gr[0])
  count = 0

  def dfs(r,c):
    if r < 0 or c < 0 or r >= row or c >=col or gr[r][c] == '0':
      return
    gr[r][c] = '0'
    dfs(r + 1 , c) #down
    dfs(r - 1, c) #up
    dfs(r, c + 1) # right
    dfs(r,c - 1) # left  

  for r in range(row):
     for c in range(col):
       if gr[r][c] == '1':
         count += 1
         dfs(r,c)

  return count
  
#print(numberislands(grid))
grid2 =[["1","1","0","0","0","1"],
       ["0","0","0","1","0","0"],
       ["0","1","0","0","0","1"],
       ]
#print(grid2[0][2])

### when to by the stocks

v= [7,1,5]

def buystock(price):
  stock_price = price[0]
  profit =0

  for i in range(len(price)):
    if price[i] < stock_price:
      
      stock_price = price[i]
      
    else:
      sell =price[i]
      current_profit = price[i] - stock_price
      
      profit = max(current_profit, profit)

  return stock_price,sell,profit
#print(buystock(v)) 


## spiral matrix

matrix = [[2,3,4,5],
          [0,7,8,9],
          [6,7,8,9]]

def spiral_matrix(mat):
  left, right = 0 , len(mat[0])
  top, bottom = 0, len(mat)
  result =[]
  print(left,right)
  print(top,bottom)
  while left < right and top<bottom:
    for i in range(left,right):
      #print(mat[0][i])
      result.append(mat[0][i])
    top+= 1
    for i in range(top,bottom):
      #print(mat[i][right-1])
      result.append(mat[i][right-1])
    right -= 1
    for i in range(right-1,left-1,-1):
    #print(right-1,left-1)
    #print(i)
      #print(mat[bottom-1][i]) 
      result.append(mat[bottom-1][i])   
    bottom -= 1
    for i in range(bottom-1,top-1,-1):
      print("ind:",bottom-1)
      print(mat[i][left])
      result.append(mat[i][left])
    left += 1
  print(result) 

spiral_matrix(matrix)


# x=[2,3,4,5,6]
# for i in range(len(x)-1,3,-1):
#   print(i)