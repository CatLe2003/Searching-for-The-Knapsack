import os
import time
import tracemalloc
from brute_force import brute_force
from branch_and_bound import branch_bound
from local_beam import local_beam
from genetic import genetic

def read_file(input_name):
    fin = open(input_name)

    # Reading each line in file, excluding the '\n' character
    data_list = [s.strip() for s in fin.readlines()]

    capacity = int(data_list[0])
    num_classes = int(data_list[1])
    weights = data_list[2].split(', ')
    values = data_list[3].split(', ')
    labels = data_list[4].split(', ')
    items = []

    for i in range(len(weights)):
        # item(weight, value, label)
        items.append((int(weights[i]), int(values[i]), int(labels[i])))
        
    print("List items = ", items)
    fin.close()

    return items, capacity, num_classes

def write_file(output_name, result): 
    best_choice = str(result[0])
    best_combination = ', '.join(str(s) for s in result[1]) # Remove ']' character
    
    fout = open(output_name, 'w')
    fout.write(best_choice + '\n' + best_combination)
               
    fout.close()

def solver(method, input_name, output_name):
    items, max_weight, num_classes = read_file(input_name)
    result = method(max_weight, items, num_classes)
    print("Result = ", result)
    write_file(output_name, result)

if __name__ == "__main__":
    n = int(input("Enter the number of file need to test: "))
    algorithm = [("1. Brute force search", brute_force), 
                 ("2: Branch and bound", branch_bound), 
                 ("3. Local beam", local_beam),
                 ("4: Genetic algorithm", genetic),
                 ("0. Exit", 0)]

    while(True):
        os.system("cls") # Windows

        print("======================")
        for i in range(len(algorithm)):
            print(algorithm[i][0])
        print("======================")
        choice = int(input("Please enter your choice: "))

        if choice == 0:
            os.system("cls") # Windows
            break

        if choice < 0 or choice > 4:
            print("Out of range, please try again.")
            input("Press Enter to continue...")
            continue

        os.system("cls") # Windows
        print("===={}====".format(algorithm[choice - 1][0]))
        for i in range(1, n + 1):
            start_time = time.time()
            tracemalloc.start()
            
            print("File {}:".format(i))
            solver(algorithm[choice - 1][1], "./Input/INPUT_{}.txt".format(i), "./Output/OUTPUT_{}.txt".format(i))
            
            memory, peak = tracemalloc.get_traced_memory()
            tracemalloc.stop()
            end_time = time.time()
            
            print("It took %f ms" % ((end_time - start_time)*1000))
            print(f"Consumed memory =  {memory / 10**6:.4f} MB")
        
        input("Press Enter to continue...")