
#write a program for grading calculator

#A:90-100
#B:80-89
#C:70-79
#D:60-69
#F:0-59

#logic building
#input-> int
#output string
score=int(input("Enter the score:"))
if 90 <= score <= 100:
    grade='A'
    print("Your grade is :",grade)
elif 80 <= score <= 89:
    grade='B'
    print("Your grade is :",grade)
elif 70 <= score <= 79:
    grade='c'
    print("Your grade is :",grade)
elif 60 <= score <= 69:
    grade='D'
    print("Your grade is :",grade)
else:
    grade='F'
    print("Your grade is :",grade)
