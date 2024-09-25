# Write a Python program to sort (ascending and descending) a dictionary by value.

# Original dictionary :  {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
# Dictionary in ascending order by value :  [(0, 0), (2, 1), (1, 2), (4, 3), (3, 4)]
# Dictionary in descending order by value :  {3: 4, 4: 3, 1: 2, 2: 1, 0: 0}

# a={1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
# for i,j in a.items():
#     for x,y in a.items():
#         if j<y:
#             print(a.items())


n=int(input("enter n:"))
i=1
sum=1
p=1
while i<=n:
    j=1
    while j<=n:
        p=p*(1/(n-i))
        n-=1
        j+=1
    sum=sum+p
    i+=1
print(sum)




# i=1
# k=1
# while i<=5:
#     j=1
#     while j<=i:
#         print(k, end=" ")
#         j+=1
#         k+=1
#     i+=1
#     print()