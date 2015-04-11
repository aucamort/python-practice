# Write a program that outputs all the possible combinations of pennies, 
# nickels, dimes, and quarters which can add up to equal $25.  

# Essentially, you will perform what is called an 'exhaustive search' 
# algorithm, which just means you will try every possible combination of 
# pennies, nickels, dimes, and quarters, and testing to see which ones add 
# up to exactly $25. (When exhaustive searches are applied to code-breaking, 
# they are called 'brute-force' algorithms).


amount = 25.00

for a in range(amount/.01):										              			#loop for num of pennies that will add up to amount, not more (in this case, amount/.01 is 25.00/.01 = 2,500 pennies will add up to 25.00 -- the loop will repeat 2,500 times)
	for b in range(amount/.05): 										              	#loop for num of nickels that will add up to amount, not more
		for c in range(amount/.10):											              #loop for num of dimes that will add up to amount, not more
			for d in range(amount/.25):										              #loop for num of quarters that will add up to amount, not more
				if .01*a + .05*b + .10*c + .25*d == amount:					      #if the numbers of pennies, nickels, dimes, quarters add up to amount
					print a,"pennies",b,"nickels",c,"dimes",d,"quarters"
					
#count of "a" loop starts at 0, then "b" loop starts at 0, then "c" loop starts at 0, then "d" loop starts at 0 and finishes first. "c" loop will then finish after "d," and so on. that's why the first answer was 0 pennies 0 nickels 5 dimes 98 quarters. 
	
	
# Time: 10 minutes	
