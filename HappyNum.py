# Take Input from the user

def sumofdigits(n):
	res = 0
	rem = 0
	while n>0 :
		rem = n%10
		res = res + rem*rem
		n = n // 10 # truncated divsion which it omits the last value
	return res

n = int(input('enter the number:'))
# Store the input 
result = n

while result!=1 and result!=4:
	# Declaring the function
	result = sumofdigits(result)

if result == 1:
	print (n , 'Happy Number')
else:
	print(n , 'UnHappy Number')