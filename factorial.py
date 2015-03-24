n = int(raw_input("Enter an integer to calculate its factorial: "))
product = 1

for i in range(1,n+1):
	product = product * i
	i = i + 1

print product
