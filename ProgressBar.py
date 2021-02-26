import sys
from os import system, name
import math

if not (name == 'posix'):
	print('Only runs in unix')
	sys.exit()

import math
import random

s = 10000 

for i in range(s):
	random.seed(i)
	random.randint(0,100) 
	_ = system('clear')	
	f = i/s
	pc = int(round(f,2)*100)
	bs = math.floor(pc/10)
	i = bs
	j = 10 - i
	stars = ''
	while (i > 0):
		stars = stars + '*'
		i -= 1
	while (j > 0):
		stars = stars + ' '
		j -= 1
	bar = '['+stars+']'
	print(bar + ' ' + str(pc)+'% complete') 

_ = system('clear')	
print('Process completed')
