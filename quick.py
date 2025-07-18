# def partition(start,end,l1):
#     i=start
#     j = end -1
#     pivot = l1[end]
#     print("l1 -> ", l1)

#     while i < j:
#         while l1[i] < pivot:
#             i+=1
#         while l1[j] > pivot:
#             j-+1
#         if i < j:
#             l1[i],l1[j] = l1[j],l1[i]
            

#     if l1[i] > pivot:
#         l1[i],l1[end] = l1[end],l1[i]
#         return i

    
# l1=[3,5,8,1,2,9,4,7,6]
# print(partition(0,len(l1)-1,l1))

#! Stack 
# class Stack_Plates:
#     def __init__(self,maxSize):
#         self.maxSize = maxSize
#         self.stack = []

#     def push(self,val):
#         if len(self.stack) > 0 and len(self.stack[-1]) < self.maxSize:
#             self.stack[-1].append(val)
#         else:
#             self.stack.append([val])
    
#     def pop(self):
#         if len(self.stack) == 0:
#             print("No Elements...")
#         elif len(self.stack) and len(self.stack[-1]) > 0:
#             self.stack[-1].pop()
#         else:
#             self.stack.pop()
    
#     def popat(self,num):
#         if num > len(self.stack) and num  <= 0:
#             print("These is no stack num")
#         else:
#             self.stack[num-1].pop()
    
#     def pushat(self,num,val):
#         if num > len(self.stack) or num <= 0: 
#             print("No stack num")
#         else:
#             if len(self.stack[num-1]) == self.maxSize:
#                 print("Stack is full")
#             else:
#                 self.stack[num-1].append(val)
    
#     def display(self):
#         print(self.stack)

# s1= Stack_Plates(4)
# s1.push(10)
# s1.push(10)
# s1.push(30)
# s1.push(40)
# s1.push(50)
# s1.push(60)
# s1.push(70)
# s1.push(80)
# s1.push(90)
# s1.push(100)
# s1.push(110)
# s1.push(120)
# s1.push(130)
# s1.display()
# s1.pop()
# s1.display()
# s1.pop()
# s1.display()
# s1.popat(2)
# s1.display()


# ! linear search

def linear_search(ele,l1):
    for i in range(len(l1)):
        if ele == l1[i]:
            print("Element found at ->",i)
            break
    else:
        print("Not Found")

l1 = [2,5,6,7,3,9,0,1]
ele = int(input("Enter the element : "))
linear_search(ele,l1)