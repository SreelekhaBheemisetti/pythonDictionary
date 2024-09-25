# Take an input n and repeatedly find the sum of the digits of a number till you get a single digit.
# Example: 678 -> 6+7+8 = 21 -> 2+1 = 3

# n=input("enter n:")
# sum=0
# a=int(n)
# i=0
# while i<len(n):
#     b=a%10
#     sum+=b
#     a=a//10
#     i+=1
# if sum>10:
#     j=0
#     s=0
#     while j<len(str(sum)):
#         c=sum%10
#         s=s+c
#         if sum//10==0:
#            sum=(sum//10)+1
#         else:
#            sum=sum//10
#         j+=1
#     print(s)
# else:
#  print(sum)


# Take an input n, and print the first n composite numbers.
# For example for n = 4, the first 4 composite numbers are 4,6,8,9



# Write a program to find out the sum of first N terms of the following series 2+22+222+2222+.... up to N terms.
# if N=6 then this series becomes 2+22+222+2222+22222+222222 = 24,6912(output)
# if N=3 then this series becomes 2+22+222 =246(output)

# n=int(input("enter n:"))
# a=2
# ssum=""
# sum=0
# i=1
# while i<=n:
#     ssum=ssum+str(a)
#     b=int(ssum)
#     sum=sum+b
#     i+=1
# print(sum)


