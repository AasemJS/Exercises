# Code your solution here
x = "good morning"
y = 2
z = "Mumbai"
str_arithmetic = 0
try:
    p = x + y
    str_arithmetic = str_arithmetic + 1
except:
    str_arithmetic = str_arithmetic
try:
    p = x % y
    str_arithmetic = str_arithmetic + 1
except:
    str_arithmetic = str_arithmetic
try:
    p = x - y
    str_arithmetic = str_arithmetic + 1
except:
    str_arithmetic = str_arithmetic
try:
    p = x / y
    str_arithmetic = str_arithmetic + 1
except:
    str_arithmetic = str_arithmetic
try:
    p = x // y
    str_arithmetic = str_arithmetic + 1
except:
    str_arithmetic = str_arithmetic
try:
    p = x * y
    str_arithmetic = str_arithmetic + 1
except:
    str_arithmetic = str_arithmetic
try:
    p = x ** y
    str_arithmetic = str_arithmetic + 1
except:
    str_arithmetic = str_arithmetic




try:
    q = x + z
    str_arithmetic = str_arithmetic + 1
except:
    str_arithmetic = str_arithmetic
try:
    q = x % z
    str_arithmetic = str_arithmetic + 1
except:
    str_arithmetic = str_arithmetic
try:
    q = x - z
    str_arithmetic = str_arithmetic + 1
except:
    str_arithmetic = str_arithmetic
try:
    q = x / z
    str_arithmetic = str_arithmetic + 1
except:
    str_arithmetic = str_arithmetic
try:
    q = x // z
    str_arithmetic = str_arithmetic + 1
except:
    str_arithmetic = str_arithmetic
try:
    q = x * z
    str_arithmetic = str_arithmetic + 1
except:
    str_arithmetic = str_arithmetic
try:
    q = x ** z
    str_arithmetic = str_arithmetic + 1
except:
    str_arithmetic = str_arithmetic
    

print(str_arithmetic)