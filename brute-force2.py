# Modify program 1 to output the total weight of each of these combinations 
# of coins. 

# Time: 3 minutes

amount = 25.00

for a in range(amount/.01):													
	for b in range(amount/.05): 											
		for c in range(amount/.10):											
			for d in range(amount/.25):										
				if .01*a + .05*b + .10*c + .25*d == amount:					
					print (a*2.500) + (b*5.000) + (c*2.268) + (d*5.670)
					
# Weight info is from the U.S. Mint's website			
