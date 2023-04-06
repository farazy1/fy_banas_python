import sys
import math
import random
import threading
import time
import re
import sqlite3
import csv 

'''
#first example of importign a function from another file
import recursive_functions 
print(recursive_functions.factorial(4))
'''

#second example of importing a function from another file:
from recursive_functions import factorial
print(factorial(4))