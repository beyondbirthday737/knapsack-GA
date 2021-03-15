class KnapsackObjects:
    def __init__(self):
        self.objects_list = []

        with open("objetos.txt") as f:
            self.objects_list = f.read().splitlines()

    def get_objects_list(self):
        return self.objects_list

    def print_objects_list(self):
        for item in self.objects_list:
            print(item)