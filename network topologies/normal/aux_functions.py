import random 

#This function creates a random grapgh
def create_graph(graph_size):
    graph = []
    for i in range(graph_size): 
        vertex = [] 
        for j in range(graph_size): 
            vertex.append(random.randint(0, 1)) 
        graph.append(vertex) 
    for i in range(graph_size): 
        for j in range(0, i): 
            graph[i][j] = graph[j][i] 
    for i in range(graph_size): 
        graph[i][i] = 0
    return graph

# This function creates a new invidividual based on the the number of colors
def create_individual(graph_size, number_of_colors): 
    individual = [] 
    for _ in range(graph_size): 
        individual.append(random.randint(1, number_of_colors)) 
    return individual

# This function returns the fitness of a given individual on a graph
def fitness(graph, individual, graph_size):
    fitness = 0    
    for i in range(graph_size):        
        for j in range(i, graph_size):            
            if(individual[i] == individual[j] and graph[i][j] == 1): 
                fitness += 1
    return fitness 

# This function creates two childs based on two given parents
def crossover(parent1, parent2, graph_size):
    position = random.randint(2, graph_size-2)
    child1 = [] 
    child2 = [] 
    for i in range(position+1): 
        child1.append(parent1[i]) 
        child2.append(parent2[i]) 
    for i in range(position+1, graph_size): 
        child1.append(parent2[i]) 
        child2.append(parent1[i]) 
    return child1, child2 

# This function changed an individual based on a given probability value
def mutation(individual, graph_size, number_of_colors, probability):
    check = random.uniform(0, 1) 
    if(check <= probability): 
        position = random.randint(0, graph_size-1) 
        individual[position] = random.randint(1, number_of_colors) 
    return individual

# This function creates a mating pool based on the roulette wheel dynamic
def roulette_wheel_selection(population, graph, graph_size):
    total_fitness = 0
    for individual in population: 
        total_fitness += 1/(1+fitness(graph=graph, individual=individual, graph_size=graph_size)) 
    cumulative_fitness = [] 
    cumulative_fitness_sum = 0
    for i in range(len(population)): 
        cumulative_fitness_sum += 1 / (1+fitness(graph=graph, individual=population[i],graph_size=graph_size))/total_fitness 
        cumulative_fitness.append(cumulative_fitness_sum) 

    new_population = [] 
    for i in range(len(population)): 
        roulette = random.uniform(0, 1) 
        for j in range(len(population)): 
            if (roulette <= cumulative_fitness[j]): 
                new_population.append(population[j]) 
                break
    return new_population
