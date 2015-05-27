def abs_my(x):
	if x>=0:
		return x
	else:
		return -x
		
n=int(raw_input("enter a number:"))
print abs_my(n)