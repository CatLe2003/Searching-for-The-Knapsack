import itertools
from itertools import permutations

class LocalBeamSearch:
    def __init__(self, max_weight: int, 
                 num_classes: int, 
                 items: 'list[tuple(int)]'):
        self._capacity = max_weight # Knapsack's storage capacity
        self.num_classes = num_classes # number of classes (Category)
        self.items = items # item(weight, value, lables)

        self.size = len(items) # number of items, not in solution
        self.labels = num_classes #n umber of labels in the list of chosen items (For initialization). All classes must be chosen at least once.

    def calculateHeuristic(self, state): # calculate the heuristic of each generated solution
        # a solution is a sequence of character 0, 1 
        value = 0 
        weight = 0
        for i in range(self.size): # for each item in the solution
            if state[i] == '1': # if the label is chosen, mark it with 1 
                # calculate the value and weight of that item 
                weight += self.items[i][0]
                value += self.items[i][1] 
        if weight > self._capacity:
            value = 0 

        return value

    def States(self): #randomly choose a number of states (solution) to initialize 
        random_state = max([''.join(map(str, x)) for x in itertools.product([0, 1], repeat=self.size)], key=self.calculateHeuristic)
        #random_states = [random_state]*k
        return random_state
    
    def generateStates(self, sub_state): #generate new child states from random parent states
        children = [] #create a list containing all child solutions generated from parent solutions 
        #this loop is to generate new child solutions
        for i in range(self.size): 
            child = list(sub_state) #create a child solution 
            #We create a new child solution using this rule: 
            #if the label in the parent solution does exist, then erase it from the solution and vice versa 
            child[i] = '1' if child[i] == '0' else '0' #Therefore, for each iteration, we can generate a new child solution
            children.append(''.join(child)) #add the new child to the list of child solutions 
        
        return children 

    def algorithm(self, k, max_iterations): 
        random_states = [self.States()]*k 
        #sub_states = [self.States(k) for _ in range(k)] #a list of k random States whose type is string  
        best_state = max(random_states, key=self.calculateHeuristic) #choose best solution by calculating the maximum value between k solutions' values
        best_value = self.calculateHeuristic(best_state) #calculate the value of the best solution
        
        for i in range(max_iterations):
            children = []
            for state in random_states: 
                #create a list of all generated child solutions from each parent solution
                children += self.generateStates(state)
        
            #sort in descending order relying on the value of each child solution, and take k child states
            sub_states = sorted(children, key=self.calculateHeuristic, reverse=True)[:k]
            #choose from generated child solutions the best solution 
            new_best_state = max(sub_states, key=self.calculateHeuristic)
            new_best_value = self.calculateHeuristic(new_best_state)

            #if the new best value > best value, assign current best solution and value to the new best ones 
            if new_best_value > best_value:
               best_state = new_best_state
               best_value = new_best_value 
        
        chosen_items = [i for i in range(self.size) \
                        if best_state[i] == '1']
        #convert to integer 
        best_combination = [0] * self.size
        for item in chosen_items:
            best_combination[item] = 1
        return best_value, best_combination

def local_beam(max_weight, items, num_classes):
    """Local beam method for solving Knapsack problem
    - param max_weight: the capacity of knapsack
    - param items: list of tuples like: [(weight, cost, label), (weight, cost, label),...]
    - param num_classes: the class number of items
    - return: tuple like: (best cost, best combination list (contains 0 and 1))
    """               
    local_beam = LocalBeamSearch(max_weight, num_classes, items)
    result = local_beam.algorithm(k = 10, max_iterations = 1000)
    return result