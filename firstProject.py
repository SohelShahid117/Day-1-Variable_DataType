#Day-1:Python Full Course❤️ | Variables & Data Types | Lecture 1
#https://youtu.be/t2_Q2BRzeEE?si=43a2CR-rM-PKZGlA

"""
multi
line 
comment
"""
print("hello world")
a = 6
print(a)
print(2+3)
age=34
print("my name is sohel.\nmy age is:",age)
price=27.99
print(price)

print(type(a))
print(type(age))
print(type(price))

name="Sohel"
print(name)
print(type(name))

print("data type are:")
l=["int","float","str","boolean","None"]
print(l)
print(type(l))

n= None;
print(n)
print(type(n))
old = False
print(old)
print(type(old))

num1 = 166
num2 = 77
sum = num1 + num2
print(sum)
print(num1-num2)
print(num1*num2)
print(num1/num2)
print(num1%num2)

# Types of operator
print("arithmatic operator:+,-,*,/,%,**")
print("relational | comparison operator:==,!=,>,<,>=,<=")
print("assignment operator:=,+=,-=,*=,/=,%=,**=")
print("logical operator:not,and,or")
print(2**3)
print(num1==num2)
print(10/2)
print(10%2)
print(10**5)


print(True)
print(False)
# print(! False)
print(not False)
print(2>5)
print(not 2>5)
print(not(2>5))
# val1 = True
val1 = False
val2 = True
print("and opeartor is : ",val1 and val2)
print("or opeartor is : ",val1 or val2)
print((num1==num2) and (num1>num1))
print((num1==num2) or (num1>num2))

x,y=4,5
print(x+y)
x2,y2=4,"5"
print(x2+float(y2)) #9.0-->type casting-forcely apply | manually convert
print(x2+int(y2)) #9-->type casting-forcely apply | manually convert
x3,y3=4,5.0
print(x3+y3) #9.0-->type conversion
print(type(x))
print(type(str(x)))

myName = input("enter your name:")
print("my name is :",myName)

val = input("enter some value:")
print(type(val),val)
val2  = int(input("enter some value:"))
print(type(val2),val2)
val3  = float(input("enter some value:"))
print(type(val3),val3)
print(val2+val3)

firstName = input("enter your last name :")
age =int(input("enter your age :"))
marks =float(input("enter marks :"))
print("last name is :",firstName)
print("age is :",age)
print("marks is :",marks)
length = int(input("enter the length of square:"))
# print("area of square=",length*length)
print("area of square=",length**2)

n1=float(input("enter 1st number:"))
n2=float(input("enter 2nd number:"))
avg = (n1+n2)/2
print("avg is = ",avg)
print((n1>n2) or (n1==n2))