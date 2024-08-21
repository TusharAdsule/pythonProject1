#Triangle classifier
# write a program that classifies a triangle based  on its side length.
# Given three inputs values representing the length of the sides ,
# determine if the triangle is equilateral,isosceles,or if scalene:

A=float(input("Enter the length of 1st Side of triangle: "))
B=float(input("Enter the length of 2nd Side of triangle: "))
C=float(input("Enter the length of 3rd Side of triangle: "))
if A==B==C:
    print(f"Triangle is Equilateral as ALL three sides {A} , {B} ,{C} are equal")
elif A==B or A==C:
    print(f"Triangle is Isosceles as two sides {A} , {B} ,{C}  are  equal")
else:
    print(f"Triangle is Scalene as all three sides {A} , {B} ,{C} are not equal")