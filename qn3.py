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