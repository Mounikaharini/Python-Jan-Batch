#Increment loop
#1 2 3 4 5 
i=1
while i<=5:
    print(i,end=" ")
    i+=1
print()
#2 4 6 8 10
i=2
while i<=10:
    print(i,end=" ")
    i+=2
print()
#Decrement loop
# 5 4 3 2 1
i=5
while i>=1:
    print(i,end=" ")
    i-=1
print()
# 10 8 6 4 2 
i=10
while i>=2:
    print(i,end=" ")
    i-=2
print()
#N natural values
# 5 values from 8 Multiples
# 8 16 24 32 40
i=int(input("Enter the table value: "))
j=i
n=int(input("Enter the count : "))
count=1
while count<=n:
    print(i,end=" ")
    count+=1
    i+=j
    #i=5+5=10
    #i=10+5=15
    #i=15+5=20
    #i=20+5=25

# sum of digits
n = int(input("enter a number : "))
s=0
while n>0:
    m=n%10
    s=s+m
    n//=10
print(s)

#count the digits
n = int(input("enter a number : "))
count=0
while n>0:
    n//=10
    count+=1
print(count)

#armstrong number
n = int(input("enter a number : "))
n1 = n
n2 = n
digit=0
while n>0:
    n//=10
    digit+=1
s=0
while n1>0:
    m=n1%10
    s=s+(m**digit)
    n1//=10
if s==n2:
    print("armstrong number")
else:
    print("not a armstrong number")
#palindrome or not 
n=int(input("enter a number :"))
n1=n
rev=0
while n>0:
    x=n%10
    rev=(rev*10)+x
    n//=10
if n1==rev:
    print("Palindrome")
else:
    print("Not a palindrome")
#2*10=20      ->      20+5=25
#25*10=250  ->      250+1=251

#prime or not
# 2 3 5 7 11 13 17 19 23.......
n=int(input("Enter a number : "))
count=0
for i in range(2,n,1):
    if n%i==0:
        count+=1
if count==0:
    print("Prime Number")
else:
    print("Not a Prime Number")











