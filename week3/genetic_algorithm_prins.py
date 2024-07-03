import random
import string


class GeneticAlgorithm:

    def __init__(self):
        self.population_size = 10
        self.target = "bird"
        self.population = []
        self.mutation_probability = 0.3

        for _ in range(self.population_size):
            word = ''.join(random.choices(string.ascii_lowercase, k=len(self.target)))
            self.population.append(word)

    def __fitness_assignment(self):
        fitness = {}

        for word in self.population:
            score = sum(1 for x, y in zip(word, self.target) if x == y)
            fitness[word] = score

        sorted_fitness = sorted(fitness.items(), key=lambda x: x[1], reverse=True)
        return sorted_fitness

    def __selection(self, sorted_fitness):
        parents = []

        for _ in range(self.population_size):
            parent_1 = random.choice(sorted_fitness)[0]
            parent_2 = random.choice(sorted_fitness)[0]
            parents.append((parent_1, parent_2))

        return parents

    def __cross_over(self, parents):
        offspring = []

        half = int(len(self.target) / 2)
        for parent_1, parent_2 in parents:
            offspring.append(parent_1[:half] + parent_2[half:])

        return offspring

    def __mutation(self, offspring):
        mutated_offspring = []
        for child in offspring:
            if random.random() < self.mutation_probability:
                to_replace = random.randint(0, len(child) - 1)
                mutated_child = child[:to_replace] + random.choices(string.ascii_lowercase, k=1)[0] + child[to_replace+1:]
                mutated_offspring.append(mutated_child)
            else:
                mutated_offspring.append(child)
        return mutated_offspring

    def __replacement(self, mutated_offspring):
        self.population = mutated_offspring

    def __termination(self):
        return self.target in self.population

    def run(self):
        generations = 0
        while not self.__termination():
            fitness = self.__fitness_assignment()
            print(fitness)
            parents = self.__selection(fitness)
            print(parents)
            offspring = self.__cross_over(parents)
            print(offspring)
            mutated_offspring = self.__mutation(offspring)
            print(mutated_offspring)
            self.__replacement(mutated_offspring)
            print(self.population)

            generations += 1

        print(f"Found target after {generations} generations.")


if __name__ == "__main__":
    algo = GeneticAlgorithm()
    algo.run()
