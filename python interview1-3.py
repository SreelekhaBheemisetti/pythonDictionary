# Write a program to check if the given number is divisible by 5, 11, both or none.
# If it is divisible by 5 then print 5
# If it is divisible by 11 then print 11
# If it is divisible by 5 and 11 then print “Both”
# If it is not divisible by 5 and 11 th then print "None"

# n=int(input("enter n:"))
# if n%5==0 and n%11==0:
#     print("Both")
# elif n%5==0:
#     print("5")
# elif n%11==0:
#     print("11")
# else:
#     print("None")



# Accept the lengths of the three sides of a triangle to validate whether they can be the sides of a triangle 
# and then classify the triangle as equilateral (all three sides are equal), scalene (all three sides are different), 
# or isosceles (exactly two sides are equal), and then to see whether it is a right-angled triangle 
# (the sum of the squares of two sides is equal to the square of the third side.)

# a=int(input("enter a:"))
# b=int(input("enter b:"))
# c=int(input("enter c:"))
# if a==b==c:
#     print("Equilateral")
# elif ((a**2+b**2)==c**2) or ((b**2+c**2)==a**2) or ((c**2+a**2)==b**2):
#     print("Right-angled")
# elif a!=b and b!=c and c!=a:
#     print("Scalene")
# elif (a==b and c!=a) or (b==c and a!=b) or (c==a and b!=c):
#     print("isosceles")
# else:
#     print("Not a triangle")



# Input 3 numbers from the user, and print the second max without using logical operators (and, or)
a=int(input())
b=int(input())
c=int(input())
if a>b:
    if a>c:
        if b>c:
            print("b is second max")
        else:
            print("c is second max")
elif b>c:
    if b>a:
        if c>a:
            print("c is second max")
        else:
            print("a is second max")
elif c>a:
        if c>b:
            if a>b:
               print("a is  second max")
            else:
                print("b is second max")
else:
    print("no")


# if a!=b!=c:
#     if c>b>a:
#         print("b is second")
#     elif c<b<a:
#         print("b is second")
#     elif a>b>c:
#         print("b is second")
#     elif a<b<c:
#         print("b is second")
# elif b!=c!=a:
#     if b>a>c:
#         print("a is second")
#     elif c>a>b:
#         print("a is second")
#     elif c<a<b:
#         print("a is second")
#     elif b<a<c:
#         print("a is second")
# elif c!=a!=b:
#     if b>c>a:
#         print("c is second")
#     elif a>c>b:
#         print("c is second")
#     elif a<c<b:
#         print("c is second")
#     elif b<c<a:
#         print("c is second")


