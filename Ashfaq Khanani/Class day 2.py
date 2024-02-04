Python 3.12.0 (tags/v3.12.0:0fb18b0, Oct  2 2023, 13:03:39) [MSC v.1935 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
x="Allah is great"
type(X)
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    type(X)
NameError: name 'X' is not defined. Did you mean: 'x'?
type(x)
<class 'str'>
x=20
x=20.5
type (x)
<class 'float'>
x=1j
type (x)
<class 'complex'>
x = ["app;e","banana"]
type (x)
<class 'list'>
x = ("app;e","banana")
type (x)
<class 'tuple'>
x=20
type(x)
<class 'int'>
x=20.5
type (x)
<class 'float'>
x=1j
type (x)
<class 'complex'>
x = ["app;e","banana"]<class 'complex'>
SyntaxError: invalid syntax
SyntaxError: invalid syntax
SyntaxError: incomplete input
x = ["app;e","banana"]<class 'complex'>x = ("app;e","banana")x = ["app;e","banana"]
SyntaxError: invalid syntax
SyntaxError: invalid syntax
SyntaxError: incomplete input
x = ["apple","banana"]
type (x)
<class 'list'>
x = ["apple",1,"banana"]
type(x)
<class 'list'>
x = ["apple",1,20.5,5j"banana"]
SyntaxError: invalid syntax. Perhaps you forgot a comma?
x = ["apple",1,20.5,5j,"banana"]
x=range(6)
type (x)
<class 'range'>
x={"name": "Ashfaq", "age" : 45}
type (x)
<class 'dict'>
x = {"apple","banana", "Cherry"}
type (x)
<class 'set'>
x = frozenset({"apple", "banana", "Cheery"})
type (x)
<class 'frozenset'>
x = true
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    x = true
NameError: name 'true' is not defined. Did you mean: 'True'?
True
True
x=True
type (x)
<class 'bool'>
list (range (20))
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
list (range (5,20))
[5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
list (range (6))
[0, 1, 2, 3, 4, 5]
list (range (20))#first digit is starting point
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
list (range (5,20))#center digit is ending point
[5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
list (range (5,20,4))#last digit is difference point jis se vo calculate karega
[5, 9, 13, 17]
list (range (5,20,4))#last digit is difference point jis se vo calculate karega yani 5+4 = 9 9+4= 13 or 17 is liye k 20 tak 4 aa nahi sakta
[5, 9, 13, 17]
list (range (5,20,4,2))#last digit is difference point jis se vo calculate karega yani 5+4 = 9 9+4= 13 or 17 is liye k 20 tak 4 aa nahi sakta
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    list (range (5,20,4,2))#last digit is difference point jis se vo calculate karega yani 5+4 = 9 9+4= 13 or 17 is liye k 20 tak 4 aa nahi sakta
TypeError: range expected at most 3 arguments, got 4
x={"name": "Ashfaq", "age" : 45}
type (x)
<class 'dict'>
<class 'dict'>#colon se pehlay vali always key hoti hai yani name or age key hain or ye remove karsaktay hain lekin change nahi kar saktay example NIC num...value remove bhi hosakti hai or change bhi hosakti hain
SyntaxError: invalid syntax
10*10
100
10**10
10000000000
x = {"apple","banana", "Cherry"}
type x
SyntaxError: incomplete input
type (x)
<class 'set'>
x = {"2","banana", "Cherry"}
type (x)
<class 'set'>
<class 'set'>
SyntaxError: invalid syntax
<class 'set'>#ye ek value ek hi baar show hogi agar hum do baar likh bhi dain phir bhi show 1 hi hogi like 2 ya 4 ya apple sab ek hi baar aayega
SyntaxError: invalid syntax
x = {"apple","banana", "Cherry"}#ye ek value ek hi baar show hogi agar hum do baar likh bhi dain phir bhi show 1 hi hogi like 2 ya 4 ya apple sab ek hi baar aayega
type (X)
Traceback (most recent call last):
  File "<pyshell#62>", line 1, in <module>
    type (X)
NameError: name 'X' is not defined. Did you mean: 'x'?
type (x)
<class 'set'>
x={"name": "Ashfaq", "age" : 45}#colon se pehlay vali always key hoti hai yani name or age key hain or ye remove karsaktay hain lekin change nahi kar saktay example NIC num...value remove bhi hosakti hai or change bhi hosakti hain
type (x)
<class 'dict'>
x = frozenset({"apple", "banana", "Cheery"})#hum frozenset mai kuch bhi change nahi kar saktay likh dia matlab likh dia
type (x)
<class 'frozenset'>
x=True#ye bilkul true or false ki tarha hai bus true or false ka t or f capital mai hoga like True or False or is mai kisi kisam k bracket ki need nahi hai
type (x)
<class 'bool'>
x=dict(name="Ashfaq",age=36)
type (x)
<class 'dict'>
x=dict(name="Ashfaq",age=36)
x
{'name': 'Ashfaq', 'age': 36}
x=dict(name="Ashfaq",age=36)#ye humay dictionary form mai dega\
if 5 > 2;
print("Five is greater than two")
SyntaxError: invalid syntax

================================ RESTART: C:/Users/Admin1/Desktop/Ashfaq Khanani/conditional statements.py ================================
Five is greater than two

================================ RESTART: C:/Users/Admin1/Desktop/Ashfaq Khanani/conditional statements.py ================================
Five is greater than two

=== RESTART: C:/Users/Admin1/Desktop/Ashfaq Khanani/conditional statements.py ==
Five is less than two

=== RESTART: C:/Users/Admin1/Desktop/Ashfaq Khanani/conditional statements.py ==

=== RESTART: C:/Users/Admin1/Desktop/Ashfaq Khanani/conditional statements.py ==
Five is less than two
Five is less than two
SyntaxError: invalid syntax

Five is less than twoif 5 > 2;

print("Five is greater than two")if 5 > 2;
print("Five is greater than two")
SyntaxError: invalid syntax

=== RESTART: C:/Users/Admin1/Desktop/Ashfaq Khanani/conditional statements.py ==
Five is less than two
Five is greater than two
Five is greater than two
SyntaxError: invalid syntax



sadfasdf
Traceback (most recent call last):
  File "<pyshell#83>", line 1, in <module>
    sadfasdf
NameError: name 'sadfasdf' is not defined
a
expected an indented block after 'if' statement on line 7
SyntaxError: invalid syntax

===== RESTART: C:/Users/Admin1/Desktop/Ashfaq Khanani/conditional statements.py =====
Five is less than two
Five is greater than two
Five is greater than two
Five is greater than two
5 is greater than 2
five is greater than 2
Five is greater than 2
Five is greater than 2

===== RESTART: C:/Users/Admin1/Desktop/Ashfaq Khanani/conditional statements.py =====
Five is less than two
Five is greater than two
Five is greater than two
Five is greater than two
5 is greater than 2
five is greater than 2
Five is greater than 2
Five is greater than 2
Five is greater than 2
SyntaxError: invalid syntax
x=4 #x is of type int
type(x)
<class 'int'>
x=AShfaq #x is also a type of str(last assigned value hi type hogi chahay int ho str ho)
Traceback (most recent call last):
  File "<pyshell#88>", line 1, in <module>
    x=AShfaq #x is also a type of str(last assigned value hi type hogi chahay int ho str ho)
NameError: name 'AShfaq' is not defined
x=AShfaq #x is also a type of str  last assigned value hi type hogi chahay int ho str ho
Traceback (most recent call last):
  File "<pyshell#89>", line 1, in <module>
    x=AShfaq #x is also a type of str  last assigned value hi type hogi chahay int ho str ho
NameError: name 'AShfaq' is not defined
type(x)
<class 'int'>
x="Ashfaq"
type(x)
<class 'str'>
x=str(3)
x=str(3) # x will be '3'
x
'3'
x=str(3) # x will be 3
x
'3'
y = int (x)
y
3
y = x
y
'3'
x
'3'
y
'3'
z= float(x)
z
3.0
y = int (x) # y will be x yani str
# lekin
# In single statement using Multiple Vaiables
#like
a=b=c='I', 'Love', 'Paksitan'
print (a,b,c)
('I', 'Love', 'Paksitan') ('I', 'Love', 'Paksitan') ('I', 'Love', 'Paksitan')

===== RESTART: C:/Users/Admin1/Desktop/Ashfaq Khanani/conditional statements.py =====
Five is less than two
Five is greater than two
Five is greater than two
Five is greater than two
5 is greater than 2
five is greater than 2
Five is greater than 2
Five is greater than 2
I Love Paksitan

===== RESTART: C:/Users/Admin1/Desktop/Ashfaq Khanani/conditional statements.py =====
Five is less than two
Five is greater than two
Five is greater than two
Five is greater than two
5 is greater than 2
five is greater than 2
Five is greater than 2
Five is greater than 2
('I', 'Love', 'Paksitan') ('I', 'Love', 'Paksitan') ('I', 'Love', 'Paksitan')

===== RESTART: C:/Users/Admin1/Desktop/Ashfaq Khanani/conditional statements.py =====
Five is less than two
Five is greater than two
Five is greater than two
Five is greater than two
5 is greater than 2
five is greater than 2
Five is greater than 2
Five is greater than 2
Traceback (most recent call last):
  File "C:/Users/Admin1/Desktop/Ashfaq Khanani/conditional statements.py", line 18, in <module>
    a,b=c='I', 'Love', 'Paksitan'
ValueError: too many values to unpack (expected 2)

===== RESTART: C:/Users/Admin1/Desktop/Ashfaq Khanani/conditional statements.py =====
Five is less than two
Five is greater than two
Five is greater than two
Five is greater than two
5 is greater than 2
five is greater than 2
Five is greater than 2
Five is greater than 2
I Love Paksitan
.

===== RESTART: C:/Users/Admin1/Desktop/Ashfaq Khanani/conditional statements.py =====
Five is less than two
Five is greater than two
Five is greater than two
Five is greater than two
5 is greater than 2
five is greater than 2
Five is greater than 2
Five is greater than 2
I Love Paksitan
ILovePaksitan
ILovePaksitan
Traceback (most recent call last):
  File "<pyshell#112>", line 1, in <module>
    ILovePaksitan
NameError: name 'ILovePaksitan' is not defined
a,b,c='I', 'Love', 'Paksitan'
print (a,b,c) # agar space karni hai to , use karain
I Love Paksitan
print (a+b+c) # agar + use karegnay to space khatam hojayegi
ILovePaksitan
"Pakistan"*25
'PakistanPakistanPakistanPakistanPakistanPakistanPakistanPakistanPakistanPakistanPakistanPakistanPakistanPakistanPakistanPakistanPakistanPakistanPakistanPakistanPakistanPakistanPakistanPakistanPakistan'
a-5
Traceback (most recent call last):
  File "<pyshell#117>", line 1, in <module>
    a-5
TypeError: unsupported operand type(s) for -: 'str' and 'int'
a=5
b=6
print (a+b)
11
c="Pakistan"
d=30
print (c+d)
Traceback (most recent call last):
  File "<pyshell#123>", line 1, in <module>
    print (c+d)
TypeError: can only concatenate str (not "int") to str
print (c,d)
Pakistan 30
#yaha + karnay par print nahi hoga or naa hi add hoga bcz Pakistan or num dono alag type hain agar saath print karna hai to , use karna hoga
x=2
y=7.9
z=complex(4,5)
z
(4+5j)
z=complex(4,5) # yaha auto j agayega bcz ye complex type hai
print (x)
2
print y
SyntaxError: incomplete input
print (y)
7.9
print (z)
(4+5j)
z = complex(4,-5)
print(z)
(4-5j)
a=float(x)
b=int(y)
c=complex (X)
Traceback (most recent call last):
  File "<pyshell#139>", line 1, in <module>
    c=complex (X)
NameError: name 'X' is not defined. Did you mean: 'x'
c=complex(x)
print (type(a,b,c))
Traceback (most recent call last):
  File "<pyshell#141>", line 1, in <module>
    print (type(a,b,c))
TypeError: type.__new__() argument 1 must be str, not float
print(a)
2.0
print(b)
7
print(x)
2
print(c)
(2+0j)
print(x)
2
print(z)
(4-5j)
y=int(x)
y
2
z=int("a")
Traceback (most recent call last):
  File "<pyshell#150>", line 1, in <module>
    z=int("a")
ValueError: invalid literal for int() with base 10: 'a'
# hum string ko int mai change nahi karsaktay lekin int ko str mai change kar saktay hain
