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