import random
import string

class GeneticAlgorithm:

    def __init__(self, target, population_size):  # Corrected the constructor method name
        self.population = []
        self.population_size = population_size
        self.target = target
        self.target_length = len(self.target)

    def initialisation(self):
        for _ in range(self.population_size):
            word = ''.join(random.choices(string.ascii_lowercase, k=self.target_length))
            self.population.append(word)
        print("Returned population")
        return self.population

    def fitness(self, population):
        population_fitness = []
        for individual in population:
            population_fitness.append([individual, sum(1 for a, b in zip(individual, self.target) if a == b)])
        return population_fitness

    def selection(self):
        parents = []
        for _ in range(self.population_size):  # Generate half as many pairs as population size
            parent1 = random.choice(self.population)
            parent2 = random.choice(self.population)
            parents.append((parent1, parent2))
        return parents

    def cross_over(self, parents):
        offspring = []
        for parent1, parent2 in parents:
            crossover_point = random.randint(1, self.target_length - 1)
            child1 = parent1[:crossover_point] + parent2[crossover_point:]
            child2 = parent2[:crossover_point] + parent1[crossover_point:]
            child_choice_var = random.randint(1,10)
            if child_choice_var >5:
                offspring.append(child1)
            else:
                offspring.append(child2)
        return offspring

    def mutation(self, offspring):
        mutated_offspring = []
        for child in offspring:
            mutated_child = []
            for char in child:
                if random.random() < 0.3:
                    # random_index = random.randint(0, len(self.target) - 1)
                    # mutated_char = random.choice(self.target[random_index])
                    mutated_char = random.choice(string.ascii_lowercase)
                else:
                    mutated_char = char
                mutated_child.append(mutated_char)
            mutated_offspring.append(''.join(mutated_child))
        return mutated_offspring

    def replacement(self, offspring):
        self.population = offspring

    def termination_criteria(self):
        population_fitness = self.fitness(self.population)
        flag = False
        for individual, fitness in population_fitness:
            if fitness == self.target_length:
                flag = True
                break
        return flag

    def run(self):
        count = 0
        self.initialisation()
        print("Initial population: ")
        print(self.population)
        while True:
            count += 1
            parents = self.selection()
            offsprings = self.cross_over(parents)
            mutated_offsprings = self.mutation(offsprings)
            self.replacement(mutated_offsprings)
            print("\nReplaced population: ")
            print(self.population)
            self.termination_criteria()
            if self.termination_criteria():
                print(f"\nTarget achieved in attempt no: {count}")
                break


genetic_algorithm = GeneticAlgorithm("bird", 100)
genetic_algorithm.run()




