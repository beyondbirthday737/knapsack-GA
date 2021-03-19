from knapsack import Knapsack
from extract_objects import Objects


if (__name__ == '__main__'):
    objects = Objects()    
    knapsack = Knapsack(400, 20, 800, objects)
    knapsack.start()