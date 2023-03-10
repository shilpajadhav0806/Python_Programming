#Print a to z alphabets capital nd small:
def alphabets():
    i=0
    while(i<=25):
        print(chr(65+i))
        i=i+1
alphabets()

print("#"*70)

#natural no in revers order:
def revers_function():
    a=int(input("enter a no"))
    i=a
    while(i>=1):
        print(i)
        i=i-1
revers_function()

print("#"*70)

#prime no:
def prime_no():
    n=int(input("enter a no"))
    i=2
    x=0
    while(i<n):
        if n%1==0:
            x=1
        i=i+1
    if x==0:
        print("its a prime no")
    else:
        print("its not aprime no")
        
prime_no()







