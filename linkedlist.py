class Listnode:
    def __init__(self,val=0,next=None):
        self.val = val
        self.next = None

def createlinklist(val):
    dummy = Listnode()
    tail = dummy

    for v in val:
        tail.next = Listnode(v)
        tail = tail.next
    return dummy.next

l1 = createlinklist(['1','2','4','6'])
l2 = createlinklist(['3','7','9','10'])

def mergelinklists(l1,l2):
    dummy = Listnode()
    tail = dummy

    while l1 and l2:
        if l1.val < l2.val:
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next
    tail = tail.next

    ## appending the remaining
    tail.next = l1 if l1 else l2

    return dummy.next

#merged = mergelinklists(l1,l2)

# while merged:
#     print(merged.val, end='->')
#     merged = merged.next

def removeelement(value):
    temp = head

    while head:
        if temp.next.val== value:
            temp.next == temp.next.next
    return temp

def middlelink(head):
    fast, slow = head
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
    return slow

def linkedcycle(head):
    fast , slow = head
    while fast and fast.next:
        fast = fast.next.next
        slow = slow .next
        if slow == fast:
            return True
    return False

def reverselist(head):
   next = None
   curr = head
   prev = None
   result =[]

   while curr != None:
       result = result.append(curr.data)
       next = curr.next
       curr.next = prev
       prev = curr
       curr = next

       result = result[::-1]
   return result

def palindromelink(head):
    fast, slow = head
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next

    prev = None
    while slow:
        temp = slow.next
        slow.next = prev
        prev = slow
        slow = temp
        
    left , right = head , prev
    while right:
        if left.data != right.data:
            return False
        left = left.next
        right = right.next
    return True

def revreselink2(head,left,right):
    dummy = Listnode(0)
    dummy.next = head
    curr = dummy

    for _ in range(left-1):
        prev = prev.next

    curr = prev.next
    for _ in range(right-left):
        temp = curr.next
        curr.next = temp.next
        temp.next = prev.next
        prev.next = temp

    return dummy.next 


