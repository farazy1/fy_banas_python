import sys
import math
import random
import threading
import time
from functools import reduce


'''hello world demo
python review
'''
print("Hello World ")

'''multi line comment
works good
'''
v1 = (
    1 + 2
    + 3
)
print (v1)

v2 = (
    1 + 2 \
    + 3
)
print (v2)

# below is not recommended ( multiple line sof code on one line
v1 = 5; v1 = v1-1; v1 = v1+1 ; print (v1)

#python types
#integers, floats, complex numbers, strings, booleans

print(type(10))
print(sys.maxsize)

print(sys.float_info.max)
# floats become inacurate if more then 15 decimal place arithmatic is done
f1 = 1.1111111111111111
f2 = 1.1111111111111111
print (f1 + f2)

# complex numbers have a real + imaginary part
cn1 = 5 + 6j
print(cn1)

b1 = False
str1 = "Escape Sequences \' \" \t \\ \n"
str2 = '''Triple quoted ' " '''

#type casting works 
print("Cast", type(int(5.4)))
print("Cast", type(str(5.4)))
print("Cast", type(chr(97)))
print("Cast", type(ord('a')))

print(21, 22, 2023, sep='/')
print("No Newline", end='')
print("\n%04d %s %.2f %c" % (1, "Hello", 3.14, 'a'))
print("5 + 2 =", 5 + 2)
print("5 - 2 =", 5 - 2)
print("5 * 2 =", 5 * 2)
print("5 / 2 =", 5 / 2)
print("5 % 2 =", 5 % 2)
print("5 ** 2 =", 5 ** 2)
print("5 // 2 =", 5 // 2)
print("5 > 2 =", 5 > 2)
print("5 < 2 =", 5 < 2)
print("5 == 2 =", 5 == 2)
print("5 != 2 =", 5 != 2)
print("5 >= 2 =", 5 >= 2)
print("5 <= 2 =", 5 <= 2)
print("5 and 2 =", 5 and 2)
print("5 or 2 =", 5 or 2)
print("not 5 =", not 5)
print("not False =", not False) 

print("Random", random.randint(1,101))
print("math.inf > 0", math.inf > 0)
print("math.inf < 0",math.inf < 0)
print("math.inf == math.inf",math.inf == math.inf)
print("math.inf != math.inf",math.inf != math.inf)
print("math.nan == math.nan",math.nan == math.nan)


age = 30 
if age > 21:
    print("You can drive a tractor trailer")
elif age >= 16:
    print("You can drive a car")
else: 
    print("You can't drive")

if age < 5:
    print("You are a baby")
elif (age >= 5) and (age <= 6):
    print("You are a kid")
elif (age >= 7) and (age <= 13):
    print("You are a teenager")
else:
    print("You are an adult")

canVote = True if age >= 18 else False
print("Can Vote", canVote)

print(r"I'll be ignored \n")

print("I'll not be ignored \n")
print("Hello" + "You")
str3 = "Hello " + "You"
print("Length:", len(str3))
print("First 3:", str3[0:3])
print("Every other:", str3[0:-1:2])
str3 = str3.replace("Hello", "Goodbye")
print(str3)
str3 = str3[:8] + "y" + str3[9:]
print(str3) 
print("you" in str3) #searching for the word "you" in the string
print("You index:",str3.find("you"))
print("      [Hello]       ".strip())
print(" ".join(["Some", "Words"]))
print("A string".split(" "))
int1 = int2 = 5
print(f'{int1} + {int2} = {int1 + int2}')
print('{int1} + {int2} = {int1 + int2}')
print('int1 + int2 =', int1 + int2)



