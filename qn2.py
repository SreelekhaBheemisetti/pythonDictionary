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
