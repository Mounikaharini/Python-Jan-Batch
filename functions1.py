a=40
#global variable

def add():
    a=10      #local variable
    b=10
    print(a+b)
add()

def sub():
    a=10      #local variable
    b=10
    print(a-b)
sub()

def multiply():
    a=10      
    b=10
    print(a*b)
multiply()

def add(v1,v2):   #parameter
    print(v1+v2)
a=int(input("Enter a number :"))
b=int(input("Enter a number :"))
add(a,b)   #argument

def calc(v1,v2):
    print("Addition :",v1+v2)
    print("Subtraction :",v1-v2)
    print("Multiplication :",v1*v2)
    print("Division :",v1/v2)
a=int(input("Enter a number :"))
b=int(input("Enter a number :"))
calc(a,b)

def palindrome(s):
    if s==s[::-1]:
        print("Palindrome")
    else:
        print("Not palindrome")
s=input("Enter a string :")
palindrome(s)

#return type
def add(a,b):
    return a+b
s=add(10,20)
print(s)

#with return with parameter

def function1(a,b,c):
    return a+b+c
o1=function1(10,10,10)
print(o1)

#with return without parameter

def function2():
    a,b,c=20,20,30
    return a+b+c
o2=function2()
print(o2)

#without return with parameter
def function3(a,b,c):
    print(a+b+c)
function3(10,10,10)

#without return without parameter

def function4():
    print(10+10+10)
function4()











