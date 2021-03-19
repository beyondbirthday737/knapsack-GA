import random
from extract_objects import Objects


class Knapsack:
    def __init__(self, total_individual, total_chromosomes, total_generations, objects):
        self.total_individual = total_individual
        self.total_chromosomes = total_chromosomes
        self.total_generations = total_generations
        self.objects = objects.get_objects_list()
        
        self.population = None
        self.fitness_list = []
        self.weight_list = []
        self.individual_dic = []


    def first_population(self):
        """this function create a random populartion"""
        self.population = [[0 for i in range(self.total_chromosomes)] for i in range(self.total_individual)]

        for individual in range(self.total_individual):
            for chromosome in range(self.total_chromosomes):
                self.population[individual][chromosome] = random.randint(0, 1)
            
        return self


    def calc_fitness(self, individual):
        """calculate individual fitness"""
        sum_weight = 0
        fitness = 0
        index = 1
        
        for gen in individual:
            if gen == 1 and sum_weight <= 400:
                sum_weight += int(self.objects[index].split(';')[1])
                fitness += int(self.objects[index].split(';')[2])
            index += 1

        self.weight_list.append(sum_weight)
        self.fitness_list.append(fitness)
        return fitness, sum_weight

        
    def championship(self, index_individual1, index_individual2):
        """This function select the best individual"""
        if(abs(self.fitness_list[index_individual1]) > abs(self.fitness_list[index_individual2])):
            winner_index = index_individual1
        else:
            winner_index = index_individual2

        return winner_index


    def mutation(self, index_individual):
        """this function is responsible for making a mutation in the individual"""
        
        mutated_index = random.randint(0, self.total_chromosomes - 1)

        if self.population[index_individual][mutated_index] == 0:
            self.population[index_individual][mutated_index] = 1
        else:
            self.population[index_individual][mutated_index] = 0

        return self


    def crossover(self, index_individual1, index_individual2):
        crossover_index = random.randint(1, self.total_chromosomes - 1)
        
        child1 = self.population[index_individual1][:crossover_index] + self.population[index_individual2][crossover_index:]
        child2 = self.population[index_individual2][:crossover_index] + self.population[index_individual1][crossover_index:]

        return child1, child2


    def print_population(self):
        for individual in range(self.total_individual):
            print(str(individual) + " - [" + ", ".join(str(f) for f in self.population[individual]) + "]")
        return self


    def write_generation_files(self, path):
            file = open(f"{path}.txt", "a")
            sorted_indiduals = sorted(self.individual_dic, key = lambda row: row['weight'])

            for individual in sorted_indiduals:
                file.write(f"{individual}\n")


    def start(self):
        print("running...")
        self.first_population()
        for generation in range(self.total_generations):
            # create a new generation and calculate fitness
            new_generation = [0 for individual in range(self.total_individual)]
            for i in range(self.total_individual):
                print(f"{self.population[i]}")
                fitness = self.calc_fitness(self.population[i])

            #Select a bests individuals 
            for i in range(self.total_individual):
                winner_individual = self.championship(i, self.total_individual -1 -i)
                new_generation[i] = self.population[winner_individual]
            
            # make mutations
            mutations = random.randint(0, self.total_individual // 2)
            for i in range(mutations):
                self.mutation(random.randint(0, mutations))
            
            #make the crossover
            childs_index = self.total_individual // 2
            for i in range(0, self.total_individual // 2, 2):
                new_generation[childs_index], new_generation[childs_index + 1] = self.crossover(i, i + 1)
                childs_index += 2

            for i in range(len(self.population)):
                self.individual_dic.append({
                    "id": i,
                    "dna": self.population[i],
                    "fitness": self.fitness_list[i],
                    "weight": self.weight_list[i]
                })

            path = f'result-files/{generation + 1}'
            self.write_generation_files(path)
            
            self.population = new_generation
            self.fitness_list = []
            self.weight_list = []
            self.individual_dic = []


