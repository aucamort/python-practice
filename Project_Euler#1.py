# Project Euler, Problem 1
# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23. Find the sum of all the multiples of 3 or 5 below 1000.

sum_multiples = 0

for i in range(3,1000,1):
  if i % 3 == 0 or i % 5 == 0:
    sum_multiples = sum_multiples + i

print sum_multiples

# Answer: 233168
