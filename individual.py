from random import randint


class Individual:
    def __init__(self, objects):
        self.codgen = None
        self.fitness = None
        self.gen_weight = None
        self.objects = objects.get_objects_list()

    def generate_random_individual(self):
        self.codgen = ""
        for _ in range(100):
            gene = (randint(0, 1))
            self.codgen = self.codgen + str(gene)

        return self

    def get_codgen(self):
        return self.codgen

    def calc_fitness(self):
        gen_list = list(self.codgen)
        weight = 0
        fitness_ind = 0
        index = 1

        for gene in gen_list:
            if (gene == "1"):
                weight = weight + int(self.objects[index].split(';')[1])
                fitness_ind = fitness_ind + \
                    int(self.objects[index].split(";")[2])

            index += 1

        self.gen_weight = weight
        self.fitness = fitness_ind

    def get_weight(self):
        return self.gen_weight
