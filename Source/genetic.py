import random

class GeneticAlgorithm:
    _populationSize = 200
    _mutationRate = 0.3
    _generations = 500

    #Initialize variables and list of items 
    def __init__(self, max_weight: int, 
                 num_classes: int, 
                 items: 'list[tuple(int)]'):
        self._capacity = max_weight
        self.num_classes = num_classes
        self.items = items
        self.n = len(items)
        self._population = [random.getrandbits(self.n) for _ in range(GeneticAlgorithm._populationSize)]
        self._bestIndividual = 0
        self._bestValue = 0

    #Calculate value for each list of items
    def Fitness(self, individual: int):
        sumValue = 0
        sumWeight = 0
        n = set()
        for i in range(self.n):
            chosen = (individual & (1 << i))
            if not chosen:
                continue

            sumWeight += self.items[-1-i][0]
            sumValue += self.items[-1-i][1]

            #If the weight is greater than capacity then return 0
            if sumWeight > self._capacity:
                return 0
            n.add(self.items[-1-i][2])


        if len(n) != self.num_classes:
            return 0
    
        if sumValue > self._bestValue:
            self._bestValue = sumValue
            self._bestIndividual = individual

        return sumValue
    
    #Select two individuals to cross over
    def Selection(self, Fitnesses: 'list[int]', tournamentSize=2):
        selected  = random.sample(range(len(self._population)), tournamentSize * 2)
        
        parent1 = 0
        maxFitness = -1
        for i in selected [:tournamentSize]:
            if Fitnesses[i] > maxFitness:
                parent1 = i
                maxFitness = Fitnesses[i]
    
        parent2 = 0
        maxFitness = -1
        for i in selected [tournamentSize:]:
            if Fitnesses[i] > maxFitness:
                parent2 = i
                maxFitness = Fitnesses[i]

        return self._population[parent1], self._population[parent2]
    
    #Perform mutation on a individual
    def Mutation(self, individual: int):
        index = random.randrange(0, self.n)
        return individual ^ (1 << index)

    # Cross over two parents to produce two children by mixing them under random ration each time
    #Example : 
    #Parent 1: 1  0  1  0  1  1  1  1  0 0
    #Parent 2: 0  1  1  0  0  1  1  1  1  1
    #Crossing point = 3,7 
    #Individual 1: 1 0 1 | 0  0  1  1 | 1 0 0
    #Individual 2: 0 1 1 | 0  1  1  1 | 1 1 1
    def CrossOver(self, parent1: int, parent2: int):
        crossingPoints = random.sample(range(1,self.n),2)
        crossingPoints.sort()
        cp1 = crossingPoints[0]
        cp2 = crossingPoints[1]
        individual1 = (parent1 & (((1 << cp1) - 1) | ((2 << (cp2 - cp1 - 1)) - 1) << cp1) |
                       (parent2 & ~(((1 << cp1) - 1) | ((2 << (cp2 - cp1 - 1)) - 1) << cp1)))
        individual2 = (parent2 & (((1 << cp1) - 1) | ((2 << (cp2 - cp1 - 1)) - 1) << cp1) |
                       (parent1 & ~(((1 << cp1) - 1) | ((2 << (cp2 - cp1 - 1)) - 1) << cp1)))
        return individual1, individual2
    #Get the best individual from the population
    def findBestIndividual(self):
        _ = [self.Fitness(individual) for individual in self._population]

        return self._bestValue, self._bestIndividual

    def solve(self, sublist: 'list[int]'=None):
        generation = 0
        while generation != GeneticAlgorithm._generations:
            Fitnesses = [self.Fitness(individual) for individual in self._population]
            population = []
      
            if sublist is not None:
                sublist.append(self._bestValue)
            population.append(self._bestIndividual)

            for _ in range(0, GeneticAlgorithm._populationSize, 2):
                parent1, parent2 = self.Selection(Fitnesses, 2)

                individual1, individual2 = self.CrossOver(parent1, parent2)

                #rarely we mutate the new generation individual to diversity 
                #population. There is 30% of chance that we mutate one individual.

                if random.random() < GeneticAlgorithm._mutationRate:
                    individual1 = self.Mutation(individual1)
                if random.random() < GeneticAlgorithm._mutationRate:
                    individual2 = self.Mutation(individual2)

                population.append(individual1)
                population.append(individual2)

            del self._population
            self._population = population
            generation += 1

        bestValue = self.findBestIndividual()
        bestCombination = ", ".join(bin(bestValue[1])[2:].rjust(self.n, '0'))
        return bestValue[0], bestCombination

def genetic(max_weight, items, num_classes):
    """Genetic algorithm method for solving Knapsack problem
    - param max_weight: the capacity of knapsack
    - param items: list of tuples like: [(weight, cost, label), (weight, cost, label),...]
    - param num_classes: the class number of items
    - return: tuple like: (best cost, best combination list (contains 0 and 1))
    """               
    best_cost = 0
    best_choice = None
    for _ in range(num_classes):
        generation = GeneticAlgorithm(max_weight, num_classes, items)
        final = []
        sol = generation.solve(final)
        if int(sol[0]) > best_cost:
            best_cost = int(sol[0])
            best_choice = [int(choice) for choice in sol[1].split(', ')]
    
    return best_cost, best_choice