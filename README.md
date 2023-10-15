# Searching for The Knapsack
## Knapsack Problem (Via GeeksforGeeks)
- Given N items where each item has some weight and profit associated with it and also given a bag with capacity W, [i.e., the bag can hold at most W weight in it]. The task is to put the items into the bag such that the sum of profits associated with them is the maximum possible. 
- Note: The constraint here is we can either put an item completely into the bag or cannot put it at all [It is not possible to put a part of an item into the bag].
## Searching Algorithms
### Brute force 
- Brute force is a simple technique that can be used to solve several searching problem. 
This algorithm generates all possible solution in problem space and choose the best 
solution. Although it can be effective for some small-size problems, using brute force 
can be challenging for solving larger problem sizes because of the exponential growth 
of search space. As a result, this can lead to massive amount of computation time and 
memory usage.
- Brute force search can be used to solve knapsack problem by generating all possible 
sublists of items, checking whether each sublist satisfies tthe weight and class 
contraints or not, and choose the maximum-value sublist. Below is a step-by-step 
process of using brute force search to solve knapsack problem: First, generate all possible sublists of items: Use binary representation to represent item. For example, if the sublist is [0,1,0,1], the chosen items are the items at index 1 and 3 then loop through all the sublists from 0 to 2n - 1, where n is the number of items. After that calculate the weight, the number of items in each class, and value for each sublist. Finally, check weight and class constraints: if the weight is less than or equal to the capacity of knapsack problem, satisfies class constraints and the value of this current sublist is greater than the current best value then updates this sublist as the best solution. Do this until there is no possible sublists and return the best solution found.
### Branch and bound
- Branch and bound is an improved method from backtracking method, which works 
better than brute force by ignoring impossible solutions. We calculate the limit (best solution) for every node and compare the limit with the current best solution before 
discovering the node. If the best in the subtree is worse than the current best, we can 
ignore this node and its subtrees.
- In the good case, we only need to compute a path through the tree and prune the 
remaining branches, but in the worst case we need to compute the entire tree.
- Branch and bound is used to find solutions of optimization problems. The optimization 
problem here is the Knapsack problem, given a set of items, each with its own weight, 
value, and classification, the goal is to determine which items are included in the 
knapsack so that the total weight is less or equal to the maximum weight of the 
knapsack and whose total value is as large as possible.
(1) Calculate the unit price for each item then sort the items in descending order.
(2) Initially, when there are no items, the bag has a total value of 0, the weight is equal to 
the maximum weight the bag can hold, the upper bound is calculated as The current weight = Total value + Weight*The unit price of the largest item.
(3) Select items to add to the bag by prioritizing the items with the largest unit price that 
Weight < The remaining weight of the bag. If the weight is exceeded, consider the next object until no one can be selected, then go to step 7.
(4) After selecting the item, recalculate the total value of the bag by the value of the added 
item. The remaining weight of the bag is equal to the previous value - Added weight, the top of the bag is equal to The total value + Weight*Unit price of the next item.
(5) If you don't choose an object, keep the previous total value and weight, the upper limit is equal to the old upper limit minus the total value + Weight * Unit price of the object.
(6) Select the branch whose bound is the largest and go back to step 3.
(7) Returns the maximum value and selected objects..
### Local Beam Search
- Local Beam Search is a heuristic search algorithm. It starts with a set of initial states 
generated randomly, then it creates all the descendants from these states. After that, 
the algorithm filters and retains suitable forms from them based on a specific metric. 
Gradually, the states will converge to an expected optimal point which can be locally 
optimal, globally optimal or the states can be stuck into the positions that cannot 
converge.
- The algorithm starts by generating a set of initial valid states (Each class must have at least one item in a certain state) and then calculate the value of each state to choose 
the best state whose value is the largest one. 
- At first, calculate: The weight of a state = total weights of all items in the state. The value of a state = total value of all items in the state. If weight > W – capacity (violate 
the constraint), set value = 0.
- After that, generate the descendants of all initial states. Calculate their weight and value and then compare them to find out the best new state of all child states. Compare best newstate with best state. Keep generating child states until reaching the best solution.
### Genetic Algorithm
- In genetic programming, a set of possible solutions (or initial generation) are randomly 
generated, and then evaluated based on a set of criteria. Those solutions that best fit the criteria are then selected, and genetic mutations are applied to create new solution variants (or subsequent generations). This new generation of variants is then evaluated and the process is repeated until a satisfactory solution is found. The process is repeated until an optimal, or best “good enough”, solution is found.
- To generate the next generation, the current generation undergoes natural selection through mini-tournaments, and the ones who are fittest reproduce to create offspring. The offspring are either copies of the parent or undergo crossover where they get a fragment from each parent, or they undergo an abrupt mutation. These steps mimic what happens in nature.
- The advantage of using genetic programming to solve the knapsack problem is that a good enough solution can be found quickly without having to exhaustively search through all possible solutions. This makes it a much more efficient approach than traditional algorithms, and allows for a much faster solution to be found.
### Demo 
- Drive: https://drive.google.com/file/d/1Opl7ksHPatC_2Ef4Tcio8PK9SlzO510Q/view?usp=sharing
- Youtube: https://youtu.be/bs_rx0HPOyU
