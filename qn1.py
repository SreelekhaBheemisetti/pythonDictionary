# Write a program to take two numbers A and B as input from the user and print the number closest to (but less than) A
# which is completely divisible by B.
# Test case 1:                      Test Case 2:
# Enter A: 34                       Enter A: 22
# Enter B: 6                         Enter B: 8
# Output: 30                       Output: 16

a=int(input("enter a:"))
b=int(input("enter b:"))
c=a//b
if a%b==0:
    print(a)
else:
    print(c*b)



# Find whether a given year is a leap year. A year is said to be a leap year 
# if it is either divisible by 4 but not by 100 or divisible by 400.
# Note: No use of logical operators allowed (and, or)
# Test Case 1:                                       Test Case 2:
# Enter Year: 2000                              Enter Year: 2025
# Output: Yes                                        Output: No
# Test case3:
# Enter year: 1900
# Output: No


year=int(input("enter year:"))
if year%4==0:
    if year%100==0:
        if year%400==0:
            print("yes")
        else:
            print("no")
    else:
        print("no")
else:
    print("no")


# Accept the age, gender (‘M’, ‘F’), and the number of days and display the wages accordingly. 
#                         If the age does not fall in any range then display the following message: 
#                         “Enter appropriate age”
# Note: No use of logical operators allowed (and, or)


# Age: 			Gender 	Wage/day
# >=18 and <30 		M 		700
#                   F		750
# >=30 and <=40 	M 		800
#                   F 		850
# 	Test case 1:
# 	Enter age: 34
# 	Enter gender: “F”
# 	Enter number of days worked: 20
# 	Output: 17000


gender=input("enter gender:")
age=int(input("enter age:"))
days=int(input("enter days"))
m18=700
f18=750
m30=800
f30=850
if gender=="m":
    if age<30:
        if age>=18:
            print(m18*days)
        else:
            print("enter appropriate age")
    elif age<=40:
        if age>=30:
            print(m30*days)
        else:
            print("enter approapriate age")
else:
    if age<30:
        if age>=18:
            print(f18*days)
        else:
            print("enter approapriate age")
    elif age<=40:
        if age>=30:
            print(f30*days)
        else:
            print("enter approapriate age")



# Write a program to categorize the shape of a quadrilateral as either a square, rhombus, rectangle, parallelogram, 
# or irregular quadrilateral, having input the lengths of the four sides and one internal angle. 
# Note: No use of logical operators allowed (and, or)
# Test case 1:
# Enter side 1: 40
# Enter side 2: 60
# Enter side 3: 40
# Enter side 4: 60
# Enter internal angle: 90
# Output: Rectangle

# Test case 2:
# Enter side 1: 50
# Enter side 2: 50
# Enter side 3: 50
# Enter side 4: 50
# Enter internal angle: 72
# Output: Rhombus

a=int(input("enter a:"))
b=int(input("enter b:"))
c=int(input("enter c:"))
d=int(input("enter d:"))
angle=int(input("enter angle:"))
if angle==90:
    if a==b==c==d:
        print("square")
    elif a==c:
        if b==d:
            print("rectangle")
    elif a==b:
        if c==d:
            print("rectangle")
    elif a==d:
        if b==c:
            print("rectangle")
elif angle<90:
    if a==b==c==d:
        print("rhombus")
    elif a==c:
        if b==d:
            print("parallelogram")
    elif a==b:
        if c==d:
            print("paralellogram")
    elif a==d:
        if b==c:
            print("parallelogram")
elif angle<180:
    if a==c:
        if b==d:
            print("parallelogram")
    elif a==b:
        if c==d:
            print("paralellogram")
    elif a==d:
        if b==c:
            print("parallelogram")  
else:
    print("irregular quadrilateral")


# Write a program for obtaining the sum of a given number of terms (n) for a given value of X in 
# the following mathematical series: (Input X and N from the user) X-(X^3)/3+(X^5)/5-(X^7)/7+(X^9)/9-.... upto n terms
# Test case 1:
# if user entered X = 2 and N= 6 the series will become -> 2-(2^3)/3+(2^5)/5-(2^7)/7+(2^9)/9-(2^11)/11 
# then output will be -141.84

n=int(input("enter n:"))
x=int(input("enter x:"))
sum=0
i=1
while n>0:
    if n%2==0:
        sum=sum+((x**i)/i)
    else:
        sum=sum-((x**i)/i)
    i+=2
    n-=1
print(sum)


# Write a program to convert decimal to binary. Take an input n, and output the binary equivalent of the number.
# Test case 1:
# Enter a number: 45
# Output: 101101

# Test case 2:
# Enter a number: 79
# Output: 1001111

n=int(input("enter n:"))
s=""
i=1
while n>0:
    a=n%2
    s=str(a)+s
    n=n//2
print(s)