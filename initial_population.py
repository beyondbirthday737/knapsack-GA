from individual import Individual
from knapsack_obj import KnapsackObjects


class InitialPopulation:
    def __init__(self):
        self.individuals_list = []
        self.objects = KnapsackObjects()

    def create_population(self):
        individual_count = 0
        while(individual_count <= 3):
            individual = Individual(self.objects)
            individual.generate_random_individual()
            individual.calc_fitness()

            if(individual.get_weight() <= 2500):
                self.individuals_list.append(individual)
                individual_count += 1

        return self

    def print_population(self):
        for individual in self.individuals_list:
            print(individual.get_codgen())
        return self

