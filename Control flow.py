'''#if statement
age=17
if age<13:
    print("You are voted")
#elif
elif age<18:
    print("you are teenager")
#else statement
else:
    print("Not voted")

#Nested conditional statement
## number odd, even, negative
num=int(input("Enter a number is:"))
if num>=0:
    print("Positive")
    if num%2==0:
        print("Even")
    else:
        print("Odd")
else:
    print("Negative")

#Example
#Leap year
year=int(input("Enter a year:"))
if year%4==0:
    if year%100==0:
        if year%400==0:
            print("Leap year")
        else:
            print("Not a leap year")
    else:
        print(" leap year")
else:
    print("Not a leap year")       
'''
#Ticket based on age and student
age=int(input("Enter a age:"))
student=input("Enter a age:")
if age<5:
    print("Free")
elif age<=12:
    print("price=10")
elif age<=16:
    if student=="yes":
        print("price=12")
    else:
        print("price=18")
else:
    print("price=20")
