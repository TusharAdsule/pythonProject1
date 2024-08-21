#task07
# #Leap year checker
#create a program that determines whether a given year is leap year.
#A leap year is divisble by 4,but not by 100 unless it is also divisible by 400.
def is_leap_year(year):
    # Check if the year is divisible by 4
    if year % 4 == 0:
        # If the year is divisible by 100, it must also be divisible by 400 to be a leap year
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

# Example usage:
year = int(input("Enter a year: "))
if is_leap_year(year):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")