import sys
import math
import random
from time import sleep

c = 100

for i in range(c):
	rep = i + 1
	sleep(0.25) 	
	flt = rep/c
	percentage = math.ceil(flt*100)
	bs = math.floor(percentage/10)
	k = bs
	j = 10 - k
	stars = ''
	while (k > 0):
		stars = stars + '*'
		k -= 1
	while (j > 0):
		stars = stars + '-'
		j -= 1
	bar = '['+stars+']'
	print(bar + ' ' + str(percentage)+'% complete.', end="\r", flush=True)


print("")
print('Process ended!')
