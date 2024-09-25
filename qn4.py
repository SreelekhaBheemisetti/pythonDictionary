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