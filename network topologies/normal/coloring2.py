from array import *
import random 
import matplotlib.pyplot as plt 
import numpy as np
from aux_functions import create_graph, create_individual, fitness, crossover, mutation, roulette_wheel_selection

Gen = np.array([]) 
Fit = np.array([]) 
n = 40
population_size = 200
graph = create_graph(graph_size=n)
number_of_colors = 30
condition = True

while(condition and number_of_colors > 0):
	average_calculation = 200	
	average_fit = []
	max_gen = 0
	while average_calculation != 0:
		average_calculation -= 1
		generation = 0
		population = [] 
		for i in range(population_size): 
			individual = create_individual(graph_size=n, number_of_colors=number_of_colors)
			population.append(individual)
		best_fitness = fitness(graph=graph, individual=population[0],graph_size=n)
		fittest_individual = population[0] 
		gen = 0
		while(best_fitness != 0 and gen != 10000): 
			gen += 1
			population = roulette_wheel_selection(population=population,
												graph=graph, graph_size=n)
			new_population = [] 
			random.shuffle(population) 
			for i in range(0, population_size-1, 2): 
				child1, child2 = crossover(parent1=population[i], 
								parent2=population[i+1], graph_size=n)
				new_population.append(child1) 
				new_population.append(child2) 
			for individual in new_population: 
				if(gen < 200): 
					individual = mutation(individual=individual, graph_size=n,
						number_of_colors=number_of_colors, probability=0.4) 
				else: 
					individual = mutation(individual=individual, graph_size=n,
						number_of_colors=number_of_colors, probability=0.2) 
			population = new_population 
			best_fitness = fitness(graph=graph, individual=population[0], graph_size=n)
			fittest_individual = population[0] 
			for individual in population:
				individual_fitness = fitness(graph=graph, individual=individual, graph_size=n)
				if(individual_fitness < best_fitness): 
					best_fitness = individual_fitness
					fittest_individual = individual 			
			Gen = np.append(Gen, gen) 
			Fit = np.append(Fit, best_fitness) 		
		if(gen > max_gen):
			max_gen = gen
		if(best_fitness != 0): 
			condition = False
			print("Graph is ", number_of_colors+1, " colorable") 
		else:			
			average_fit.append(Fit)
			Gen = [] 
			Fit = []	
	average_fit_values = []
	
	for i in range(max_gen):
		columm_count = 0
		average_fit_value = 0
		for j in range(len(average_fit)):		
			if i < len(average_fit[j]):
				average_fit_value += average_fit[j][i]
				columm_count += 1
		average_fit_value /= columm_count
		average_fit_values.append(average_fit_value)
	print("number_of_colors", number_of_colors)	
	print(average_fit_values)
	Gen = np.arange(max_gen)
	plt.plot(Gen, average_fit_values)
	plt.xlabel("generation") 
	plt.ylabel("best-fitness") 
	plt.savefig('graph'+str(number_of_colors)+'.png')
	plt.clf()	
	number_of_colors -= 5
