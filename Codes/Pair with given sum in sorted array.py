# COMPLETED WITH O(n2)
# LEARNED TWO POINTER TECHNIQUE, O(n)


# O(n2) with some optimisation
# def ranging(a,k):
#     if k > a[len(a)-2]+a[len(a)-1]:
#         return False
#     elif k<a[len(a)-1]:
#         for i in range(len(a)):
#             if a[i]>k:
#                 return i
#
# t= int(input())
# while t>=0:
#     result=[]
#     n=int(input())
#     a=list(map(int,input().split()))
#     k=int(input())
#     res=ranging(a,k)
#     if res == False:
#         print("-1")
#         break
#     if res == None :
#         res=a[len(a)-1]
#
#     for i in range(res):
#         find = k-a[i]
#         if find in a:
#             if a[i] < find:
#                 result.append(tuple((a[i],find,k)))
#             else:
#                 break
#             # a.remove(a[i])
#             # a.remove(find)
#             # print(a)
#             # print(result)
#             # res=len(a)
#     print(result)
#     t-=1


# O(n) with two pointer technique
def isPairSum(a,i,j,x):
    while i<j:
        if a[i]+a[j]==x:
            pos.append(tuple((a[i],a[j],x)))
            isPairSum(a,i+1,j,x)
            return True
        elif a[i]+a[j]<x:
            i+=1
        else:
            j-=1
    return False

t= int(input())
while t>=0:
    pos=[]
    n=int(input())
    a=list(map(int,input().split()))
    x=int(input())
    isPairSum(a,0,len(a)-1,x)
    print(pos)