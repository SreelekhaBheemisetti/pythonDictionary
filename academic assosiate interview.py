# a=int(input("enter a:"))
# b=int(input("enter b:"))
# c=int(input("enter c:"))
# d=int(input("enter d:"))
# if (a>b and a>c and a<d) or (a>b and a>d and a<c) or (a>c and a>d and a<b) :
#     print("a is second")
# elif (b>a and b>c and b<d) or (b>a and b>d and b<c) or (b>c and b>d and b<a):
#     print("b is second")
# elif (c>a and c>b and c<d) or (c>a and c>d and c<b) or (c>b and c>d and c<a):
#     print("c is second")
# else:
#     print("d is second")

# rishabh@navgurukul.org
# vinay@navgurukul.org 

# a= [10, 11, 12, 13, 14, 17, 18, 19]
# k = 30
# i=0
# while i<len(a):
#     j=i
#     while j<len(a):
#         if i<len(a):
#             if a[i]+a[j]==k:
#                 print((a[i],a[j]))
#         j+=1
#     i+=1

# a1=int(input("enter a1:"))
# a2=int(input("enter a2:"))
# a3=int(input("enter a3:"))
# b1=int(input("enter b1:"))
# b2=int(input("enter b2:"))
# b3=int(input("enter b3:"))
# if True:
#         if a1<=a2<=a3:
#             max2a=a2
#         elif a2<=a1<=a3:
#             max2a=a1
#         else:
#             max2a=a3
# if True:
#         if b1<=b2<=b3:
#             max2b=b2
#         elif b2<=b1<=b3:
#             max2b=b1
#         else:
#             max2b=b3
# print(max2a,max2b)

# a=int(input("enter a:"))
# b=int(input("enter b:"))
# c=int(input("enter c:"))
# if a==b==c:
#     print("equilateral")
# elif a!=b:
#     if b!=c:
#         if c!=a:
#             print("scalene")
# else:
#     print("isosceles")


# n=int(input("enter the number:"))
# a=n
# while a>=10:
#     sum=0 
#     while a>0:
#         r=a%10
#         sum=sum+r**2
#         a=a//10
#     a=sum
# if a==1:
#     print("happy number")
# else:
#     print("unhappy")

# n=int(input("enter the number:"))
# i=0
# reverse_num=0
# while i<n:
#     digit=n%10
#     reverse_num=reverse_num*10+digit
#     n=n//10
# print(reverse_num,end=" ")

# for x in range(1,11):
#     for y in range (1,11):
#         print(x,"*",y,"=",x*y)
#     print()

# dict={x:x**2 for x in range(5) if x%2==0}
# print(dict)



# a=[56,87,45,3,65,98,67]
# a=[1,2,3,4,5,6,7,8,9]
# a=[9,8,7,6,5,4,3,2,1]
# max=0
# sec_max=0
# third_max=0
# i=0
# while i<len(a):
#     if a[i]>max:
#         third_max=sec_max
#         sec_max=max
#         max=a[i]
#     elif a[i]>sec_max:
#         third_max=sec_max
#         sec_max=a[i]
#     elif a[i]>third_max:
#         third_max=a[i]
#     i+=1
# print(max)
# print(sec_max)
# print(third_max)