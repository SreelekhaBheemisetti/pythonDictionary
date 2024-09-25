#  Write a Python program to create a dictionary from a string.
# Note: Track the count of the letters from the string.
# Sample string : 'w3resource'
# Output: {'w': 1, '3': 1, 'r': 2, 'e': 2, 's': 1, 'o': 1, 'u': 1, 'c': 1}



# a=input("enter the string:")

# a='w3resource'
# i=0
# while i<len(a):
#     c=0
#     j=0
#     while j<len(a):
#         if a[i]==a[j]:
#             c+=1
#         j+=1
#     print(a[i],":",c,  end=",")
#     i+=1

a=int(input("enter the a:"))
b=int(input("enter the b:"))
while a<b:
     j=1
     count=0
     while j<=a:
          if a%j==0:
               count+=1
          j+=1
     if count!=2:
          print(a)
     a+=1