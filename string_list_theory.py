
a = "python"
#print(a[:len(a)])
print(a.ljust(10))
print(a.rjust(10))
print("20".zfill(5))

n = "Welcome to python Programming"
print(n.split())
print(n.split('e'))
m=n.split()
print(' '.join(m))
print(n.split('o'))
print(n.rsplit('o',1))
print(n.startswith("Wel"))
print(n.endswith("ing"))

#String Formatting

Name = "Prathika"
Course = "Python"
Batch = "11.30 - 1.30"
Hours = 30
print("The",Course," Handled By",Name,"At",Batch)

#F-string
print(f"The {Course} Handled By {Name} At {Batch}")
print(f"Hours Completed {Hours+2}")

#format()
print("The {} Handled By {} At {}".format(Course,Name,Batch))
print("The {0} Handled By {1} At {2}".format(Course,Name,Batch))
print("The {c} Handled By {n} At {b}".format(c=Course,n=Name,b=Batch))

# % percentage function
print("The %s Handled By %s At %s"%(Course,Name,Batch))
print(f"Hours Completed {Hours:.2f}")

		Mutable	Ordered	Duplicates
				
LIST		yes	yes	yes
TUPLE		no	yes	yes
SET		yes	no	no
DICT		yes	yes	key-no , value -yes

#list

a=[1,2,3,4,5]
print(a)
print(a[:])
print(a[0:3])
print(a[::-1])
a.append(6)
print(a)
a.extend([7,8])
print(a)
a.insert(0,0)
print(a)
a.remove(7)
print(a)
#del a
#print(a)
a.pop()
print(a)
a.pop(0)
print(a)
#input
x = [1,2,1,3,5,1,2,4,2,3,6,3]
'''x = set(x)
print(list(x))'''
#output
#x=[1,2,3,5,4,6]

b=[]
for i in x:
    if i not in b:
        b.append(i)
print(b)

x=[1,2,3,5]
x[3]=4
print(x)

x = [1,2,1,3,5,1,2,4,2,3,6,3]
print(x.index(5))
x.sort()
print(x)
print(x.count(1))
print(x.index(5))
print(min(x))
print(max(x))
print(sum(x))
x.reverse()
print(x)
y=[[0,00],[1,11]]
print(y[0])
print(y[1])
print(y[1][0])
