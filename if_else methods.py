#find greater no:
def function():
    a=int(input("enter 1st number"))
    b=int(input("enter 2nd number"))
    if a<b:
        print("b is greater")
    else:
        print("a is greater")

function()


#check the charachter is alphabet or not#
def function_find():
    a=input("enter a chr")
    x=ord(a)
    if 64<x<91:
        print("its a uppercase chr")
    elif 96<x<123:
        print("its a lowercase chr")
    else:
        print("its a digit or no")

function_find()


#Check the leap year:
def function_yr():
    yr = int(input("enter a year:"))
    if (yr%400==0) and (yr%100==0):
        print(f"{yr}: its not a leap year")
    elif (yr%4==0) and (yr%100!=0):
        print(f"{yr}: its a leap year")
    else:
        print(f"{yr}: its not a leap year")

function_yr()



