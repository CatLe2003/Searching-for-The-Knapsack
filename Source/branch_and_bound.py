class Node:
    def __init__(self, level, weight, value, items, classItems):
        self._level = level
        self._weight = weight
        self._value = value
        self._items = items
        self._classItems = classItems
        self._bound = 0

def BranchBound(node, num_items, capacity, items, num_classes):
    if node._weight > capacity:
        return 0
    boundValue = node._value
    boundWeight = node._weight
    classItems = node._classItems[:]
    n = len(items)
    for i in range(node._level,n):
        if boundWeight + items[i][0] <= capacity:
            boundWeight += items[i][0]
            boundValue += items[i][1]
            classItems[items[i][2] - 1] += 1
        else:
            break

    if boundWeight < capacity:
        preClass = items[node._level - 1][2]
        for i in range(node._level,n):
            if items[i][2] == preClass:
                boundValue += items[i][1]
                classItems[items[i][2] - 1] += 1
                if boundWeight + items[i][0] >= capacity:
                    break
    for j in range(num_classes):
        if classItems[j] == 0:
            for i in range(node._level,num_items):
                if items[i][2] == j + 1:
                    boundValue += items[i][1]
                    break
    return boundValue
class BranchAndBound:
    def __init__(self, max_weight : int, num_classes: int, items : 'list[tuple(int)]'):
        self._capacity = max_weight
        self._num_classes = num_classes
        self._items = items
    
    def solve(self):
        n = len(self._items)
        bestValue = 0
        bestItems = [0] * n
        root = Node(0, 0, 0, [], [0] * self._num_classes)
        q = [root]

        while q:
            node = q.pop(0)
            if node._level == n:
                if node._value > bestValue:
                    bestValue = node._value
                    bestItems = node._items
                continue

            if node._bound < bestValue:
                continue
            leftClassItems = node._classItems[:]
            leftNodeWeight = node._weight + self._items[node._level][0]
            leftNodeValue = node._value + self._items[node._level][1]
            leftNodeItems = node._items + [node._level]

            left = Node(node._level + 1, leftNodeWeight, leftNodeValue, leftNodeItems, leftClassItems)
            left._bound = BranchBound(left, n, self._capacity, self._items, self._num_classes)

            if left._bound >= bestValue and left._weight <= self._capacity:
                q.append(left)

            right = Node(node._level + 1, node._weight, node._value, node._items, node._classItems[:])
            right._bound = BranchBound(right, n, self._capacity, self._items, self._num_classes)

            if right._bound >= bestValue:
                q.append(right)
      
        return bestValue, bestItems
    
def branch_bound(max_weight, items, num_classes):
    """Branch and bounds method for solving Knapsack problem
    - param max_weight: the capacity of Knapsack
    - param items: list of tuples like: [(weight, cost, label), (weight, cost, label),...]
    - param num_classes: the class number of items
    - return: tuple like: (best cost, best combination list (contains 0 and 1))
    """               
    bb = BranchAndBound(max_weight, num_classes, items)
    result = bb.solve()
    bestValue = result[0]
    bestItems = result[1]
    n = len(items)
    sol = [0]* n
    
    for i in bestItems:
        sol[i] = 1
    result = (bestValue,sol)

    return result