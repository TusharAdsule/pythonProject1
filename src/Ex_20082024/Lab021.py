#problem to find max between 3 numbers

#logica building
#1 user input-> 3 int
#output return max number

#logic
#num1>num2


num1=int(input("enter te value for number1:"))
num2=int(input("enter te value for number2:"))
num3=int(input("enter te value for number3:"))
if num1==num2==num3:
    print("num1, num2  and num3 5are equals")
elif num1>num2 and num1>num3:
    print("Max number is num1:",num1)
elif num2>num1 and num2>num3:
    print("Max number is num2:", num2)
else:
    print("Max number is num3:", num3)