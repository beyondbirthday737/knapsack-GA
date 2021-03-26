<h2>What is Genetic algorithms ?</h2>

A genetic algorithm is a search heuristic that is inspired by Charles Darwin’s theory of natural evolution. This algorithm reflects the process of natural selection where the fittest individuals are selected for reproduction in order to produce offspring of the next generation.



<a href='https://pastmike.com/what-is-a-genetic-algorithm/'>
  <img src='https://pastmike.com/wp-content/uploads/2018/08/genetic.png' >
</a>



<h2>Knapsack problem</h2>

The backpack problem Knapsack problem is a combinatorial optimization problem . The name is given due to the model of a situation in which it is necessary to fill a backpack with objects of different weights and values. The goal is to fill the backpack with the highest possible value, not exceeding the maximum weight.


<a href='https://medium.com/bigdatarepublic/genetic-algorithms-in-practice-63bcdc552fbf'>
  <img src='https://miro.medium.com/max/682/0*Um3SJ8TMyxZSRZjY.png'>
</a>


For more details see [Wikipedia](https://en.wikipedia.org/wiki/Knapsack_problem).


<h2>Solving the Knapsack problem</h2>

<h3>First Population</h3>

First step is creating an initial population. N backpacks will be filled with random items until the weight limit is reached.

```python
import random
from extract_objects import Objects
import csv
import os


class Knapsack:
    def __init__(self, total_individual, total_chromosomes, total_generations, mutation_rate, crossover_rate, elite,  pack_weigth_limit, objects):
        self.total_individual = total_individual
        self.total_chromosomes = total_chromosomes
        self.total_generations = total_generations
        self.mutation_rate = mutation_rate
        self.crossover_rate = crossover_rate
        self.elite = elite
        self.pack_weigth_limit = pack_weigth_limit
        self.objects = objects.get_objects_list()
        
        self.population = None
        self.fitness_list = []
        self.weight_list = []
        self.individual_dic = []


    def first_population(self):
        """this function create a random population"""
        self.population = [[0 for i in range(self.total_chromosomes)] for i in range(self.total_individual)]

        for individual in range(self.total_individual):
            for chromosome in range(self.total_chromosomes):
                self.population[individual][chromosome] = random.randint(0, 1)
            
        return self
```

<h3>Calculate Fitness</h3>

In this step we will implement the function to calculate the fitness score

```python
def calc_fitness(self, individual):
    """calculate individual fitness"""
    sum_weight = 0
    fitness = 0
    index = 1
        
    for gen in individual:
        if gen == 1:
            sum_weight += int(self.objects[index].split(';')[1])
            fitness += int(self.objects[index].split(';')[2])
        index += 1

    self.weight_list.append(sum_weight)
    self.fitness_list.append(fitness)
    return fitness, sum_weight

```

<h3>Tournament Selection</h3>

Tournament selection is a method of selecting an individual from a population of individuals in a genetic algorithm. Tournament selection involves running several "tournaments" among a few individuals chosen at random from the population. The winner of each tournament (the one with the best fitness) is selected for crossover

```python        
def tournament_selection(self, index_individual1, index_individual2):
    """This function select the best individual"""
    if(abs(self.fitness_list[index_individual1]) > abs(self.fitness_list[index_individual2])):
        winner_index = index_individual1
    else:
        winner_index = index_individual2
        
    return winner_index

```
