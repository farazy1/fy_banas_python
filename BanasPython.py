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

print("A String".lower())
print("A String".upper())
print("isalnum","[A String 123]","A String 123".isalnum())
print("isalnum","[0123]","0123".isalnum())
print("isalnum","[0123 ]","0123 ".isalnum())
print("isalpha","[A String]","A String".isalpha())
print("isalpha","[AString]","AString".isalpha())
print("isdigit","[0123]","0123".isdigit())
print("isdigit","[0123 ]","0123 ".isdigit())
#lists
l1 = [1, 3.14, "Faraz", True]
print("Length", len(l1))
print("1st:", l1[0])
print("last:", l1[-1])
print("1 Exists", (1 in l1))

l1[0] = 2 
l1[2:4] = ["Bob", False] #replace 3rd and "up to"4th (meaning 3rd) elements of the list
print("l1:" , "[" , l1 , "]")
l1[2:2] = ["Paul", 9] 
print("l1(after inserting new elements at 2:2):" , "[" , l1 , "]")
#also can insert explicitly
l1.insert(2,"John")
print("l1(after l1.insert(2,John)):" , "[" , l1 , "]")
# add new element to end of list
l2 = l1 + ["Egg", 4]
print('''l1(l2 = l1 + ["Egg", 4]):''' , "[" , l2 , "]")
l2.remove("Paul")
print('''l2.remove("Paul"):''' , "[" , l2 , "]")
#remove by using an index , instead of searching for the string like in l2.remove
l2.pop(0)
print('''l2.pop(0)''' , "[" , l2 , "]")
l2 = ["Egg", 4] + l1 
print('''[l2 = ["Egg", 4] + l1 ]''' , "[" , l2 , "]")
#multi demensional lists
l3 = [[1,2],[3,4],[5,6],[7,8]]
print(l3)
print("[0,0]", l3[0][0])
print("[0,1]", l3[0][1])
print("[1,0]", l3[1][0])
print("[1,1]", l3[1][1])
print("1 Exists", (1 in l3))
print("min(l3)", min(l3))

l4 = [["sam","jam","glam"],["clark","bark","mark"],["slow","mow","flow"],["car","far","ajar"]]
print(l4)
print("[0,0]", l4[0][2])
print("[0,1]", l4[1][2])
print("[1,0]", l4[2][2])
print("[1,1]", l4[3][2])
print("car Exists", ("car" in l4))

print("min([4,3,2,1])", min([4,3,2,1]))
print("max([4,3,2,1])", max([4,3,2,1]))
print("get zero and 1st index values l1[0:2]:",l1[0:2])
l1[2:2]= ["Sim",True]
l1[5:2]= ["test","set"]
l1[-1:2]= ["rome","italy"]
print("get every other value l1[::2] from the list:",l1,"\n",l1[::2])
print("print reverse from the list:",l1,"\n",l1[::-1])

#while loop needs index defined outside of while loop
w1 = 1
while w1 < 5:
    print(w1)
    w1 += 1
print("~~~~~")
w2 = 0 
while w2 <= 20:
    if w2 % 2 == 0:
        print(w2)
    elif w2 == 9:
        break
    else:
        w2 += 1 
        continue
    w2 +=1

l4 = [1, 3.14, "Derek"]
while len(l4):
    print(l4.pop(0))

for x in range(0,10):
    print(x,' ', end="")
print()

l4 = [1, 3.14, "Derek"]

for x in l4:
    print(x)

for x in [2,4,6]:
    print(x)

l5 = [6, 9, 12]
itr = iter(l5)
print(next(itr))
print(next(itr))

print(list(range(0,5)))
print(list(range(0,10,2)))


num_list = [[1,2,3], [10,20,30], [100,200,300]]

for x in range(0,3):
    for y in range(0,3 ):
        print(num_list[x][y])

t1 = (1, 3.14, "Derek")
print("Length", len(t1))
print("1st", t1[0])
print("Last", t1[-1])
print("1st 2", t1[0:2])
print("every other", t1[0::2])
print("reverse", t1[::-1])


heroes = {
    "Superman": "Clark Kent", 
    "Batman": "Bruce Wayne"
}
'''
villains = dict ([
    ("Lex Luthor", "Lex Luthor"),
    ("Loki"), ("Loki")
])
'''

print("Length", len(heroes))
print(heroes["Superman"])
heroes["Flash"] = "Barry Allan"
heroes["Flash"] = "Barry Allen"
print(list(heroes.items()))
print(list(heroes.keys()))
print(list(heroes.values()))

del heroes["Flash"]
print(heroes.pop("Batman"))
print(list(heroes.items()))
print("Superman" in heroes)


heroes = {
    "Superman": "Clark Kent", 
    "Batman": "Bruce Wayne"
}

for k in heroes:
    print(k)


print(list(heroes.items()))

for v in heroes.values():
    print (v)

d1 = {"name": "Bread", "price": .88}
print("%(name)s costs $%(price).2f" %d1)
s1 = set (["Derek", 1])
s2 = {"Paul", 1}

print("Length",len(s2))

s3 = s1|s2 
print (s3)
s3.add("Doug")
s3.discard("Derek")
print (s3)
print("Random", s3.pop())
print (s3)
s3 |=s2
print (s3)
print(s1.intersection(s2))
print(s1.symmetric_difference(s2))
print(s1.difference(s2))
s3.clear
print (s3)
s4 = frozenset(["Paul", 7]) 


def get_sum(num1: int = 1, num2: int = 1 ):
    return num1 +num2 

print(get_sum(5,4))
def get_sum2(*args):
    sum = 0 
    for arg in args:
        sum += arg
    return sum
print(get_sum2(1,2,3,4))

def next_2(num):
    return num + 1, num + 2

i1, i2 = next_2(5) 
print(i1, i2)

def mult_by(num):
    return lambda x: x * num 
print("3*5=", (mult_by(3)(5)))

def mult_list(list, func):
    for x in list:
        print(func(x))

def mult_list(list, func):
    for x in list:
        print(func(x))
mult_by_4 = mult_by(4)
mult_list(list(range(0, 5)), mult_by_4)

power_list = [lambda x: x ** 2,
              lambda x: x ** 3]
