class BruteForce:
    def __init__(self, max_weight: int, num_classes: int, items: 'list[tuple(int)]') -> None:
        self._capacity = max_weight
        self._numClasses = num_classes
        self._items = items
    
    def solve(self):
        n = len(self._items)
        bestItem = [0] * n
        bestValue = 0

        for i in range(2**n):
            item = []
            weight = 0
            cntClass = {}

            for j in range(n):
                if(i >> j) & 1:
                    item.append(j)
                    weight += self._items[j][0]
                    if self._items[j][2] in cntClass:
                        cntClass[self._items[j][2]] += 1
                    else:
                        cntClass[self._items[j][2]] = 1

            if weight <= self._capacity or all(c in cntClass for c in range(1, n+1)):
                # Calculate value for items
                sumValue = sum(self._items[j][1] for j in item)
                # Update maximum value and items
                if sumValue > bestValue:
                    bestValue = sumValue
                    for i in item:
                        bestItem[i] = 1

        return bestValue, bestItem

def brute_force(max_weight, items, num_classes):
    """Brute force method for solving knapsack problem
    - param max_weight: the capacity of knapsack
    - param num_classes: the class number of items
    - param items: list of tuples like: [(sumWeight, cost), (sumWeight, cost),...]
    - return: tuple like: (best cost, best combination list (contains 0 and 1))
    """
    bf = BruteForce(max_weight, num_classes, items)
    result = bf.solve()
    return result