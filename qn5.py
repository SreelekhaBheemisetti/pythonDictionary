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