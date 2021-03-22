from knapsack import Knapsack
from extract_objects import Objects



if (__name__ == '__main__'):
	total_individual = 400
	total_chromossomes = 20
	total_generation = 800
	mutation_rate = 0.1
	crossover_rate = 0.9
	elite = 20
	pack_weight_limit = 400
	objects = Objects()

	knapsack = Knapsack(total_individual, total_chromossomes, total_generation, mutation_rate, crossover_rate, elite, pack_weight_limit,objects)
	knapsack.start()