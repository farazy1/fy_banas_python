import sys
import math
import random
import threading
import time
#example of pythons built in support for regex
import re

if re.search("ape", "The ape at the apex"):
    print("There is an ape")

allApes = re.findall("ape", "The ape at the apex") 
for i in allApes:
    print(i)

the_str = "The ape at the apex"
for i in re.finditer("ape.", the_str): #search for all "ape" including the extra ending character
    loc_tuple = i.span() #return the tuple - start and endposition of the match
    print("start and end position of the match: ",loc_tuple) 
    print("print the matched string by slicing: ", the_str[loc_tuple[0]:loc_tuple[1]])