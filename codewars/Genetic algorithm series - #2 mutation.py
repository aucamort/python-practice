## Genetic Algorithm Series - #2 Mutation

## Mutation is a genetic operator used to maintain genetic diversity from one generation of a 
## population of genetic algorithm chromosomes to the next.

## A mutation here may happen on zero or more positions in a chromosome. It is going to check 
## every position and by a given probability it will decide if a mutation will occur.

## A mutation is the change from 0 to 1 or from 1 to 0.


from random import random


def mutate(chromosome, p):
    for i, base in enumerate(chromosome):  # enumerate to access index
        n = random()
        if n < p:  # if random num is less than probability, mutate
            if base == '1':
                chromosome = chromosome[0:i] + '0' + chromosome[i+1:]
            else:
                chromosome = chromosome[0:i] + '1' + chromosome[i+1:]
    return chromosome
