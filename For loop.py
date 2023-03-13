#Display 1st ten natural no:
def function1():
  print("1st ten natural no:")
  for i in range(1,11):
    print(i)
function1()


#sum of natural no:
def function2():
    no=int(input("enter a no"))
    total=0
    for i in range(1,no+1):
        total=total+i
    print("sum of natural no 1to{0}={1}".format(no,total))
function2()


#even no:
def function3():
    max=int(input("enter any maximum no:"))
    for no in range(1,max+1):
        if no%2==0:
          print("{0}".format(no))
function3()



#Odd no:
def function4():
     max=int(input("enter any maximum no:"))
     for no in range(1,max+1):
        if no%2!=0:
          print("{0}".format(no))
function4()


