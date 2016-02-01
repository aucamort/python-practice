## Genetic Algorithm Series - #3 Crossover

## In genetic algorithms, crossover is a genetic operator used to vary the programming of 
## chromosomes from one generation to the next. The one-point crossover consists in swapping 
## one's cromosome part with another in a specific given point. In this kata you have to 
## implement a function crossover that receives two chromosomes chromosome1, chromosome2 
## and a zero-based index and it has to return an array with the crossover result on both 
## chromosomes [chromosome1, chromosome2].

## Example: 
## crossover('111000', '000110', 3) should return ['111110', 000000']

def crossover(chromosome1, chromosome2, index):
    if index > (len(chromosome1) - 1) or index > (len(chromosome2) - 1):
        pass
    else:
        crossee = chromosome1[index:]
        chromosome1 = chromosome1[:index] + chromosome2[index:]
        chromosome2 = chromosome2[:index] + crossee
    return [chromosome1, chromosome2]

    
