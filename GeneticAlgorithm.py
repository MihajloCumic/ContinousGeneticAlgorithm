import numpy as np
from FitnessFunction import fitness_function
from GAFunctions import radcliffe
import json
from PrintFunction import *
from Plotting import *

def genetic_alg():

    #config loading
    file = open('config.json')
    config = json.load(file)
    file.close()

    #number of genes and chromosomes, frequency of mutation
    gene_num = 33
    chromosome_num = config['chromosome_num']
    mut_rate = config['mut_rate']
    #initialization of starting population with nomralized values from range [0,1]
    starting_population = np.random.rand(chromosome_num, gene_num)

    #denormalize values to range [-3, 3]
    p_hi = 3
    p_lo = -3
    with np.nditer(starting_population, op_flags=['readwrite']) as it:
        for p_norm in it:
            p = (p_hi - p_lo) * p_norm + p_lo
            p_norm[...] = p

    #check the cost of the starting population
    starting_fitnesses = fitness_function(starting_population)

    #Mediana cost of starting population
    avg_fitness = np.median(starting_fitnesses)

    #chromosome with least cost
    best_chromosome_index = np.argmin(starting_fitnesses)
    best_fitness = starting_fitnesses[best_chromosome_index]
    best_chromosome = starting_population[best_chromosome_index]

    #printing starting results
    print_results(best_fitness, np.average(starting_fitnesses),print_file = config["print_file"])


    num_of_iterations = config['num_of_iterations']

    #for plotting
    plt_best_fitness = []
    plot_avg_fitness = []

    for iteration in range(num_of_iterations):
        new_population = np.zeros(shape=(chromosome_num,gene_num))
        fitnesses = []

        #treshold cutoff
        kept_cnt = 0
        for x in range(len(starting_fitnesses)):
            if(starting_fitnesses[x] < avg_fitness):
                new_population[kept_cnt] = starting_population[x]
                kept_cnt += 1
                fitnesses.append(starting_fitnesses[x])

        #ending condition
        if(kept_cnt <= 1): break

        #chromosome with least cost
        index = fitnesses.index(best_fitness)
        best_chromosome = starting_population[index]

        #crossing and mutation
        radcliffe(kept_cnt, new_population, mut_rate)

        #preparation for next iteration
        starting_fitnesses = fitness_function(new_population)
        starting_population = new_population
        avg_fitness = np.median(starting_fitnesses)

        #checking least cost
        curr_min_fitness = np.min(starting_fitnesses)
        if(curr_min_fitness < best_fitness): best_fitness = curr_min_fitness
        
        #plotting and printing
        plt_best_fitness.append(best_fitness)
        plot_avg_fitness.append(np.average(starting_fitnesses))
        print_results(best_fitness, np.average(starting_fitnesses),iteration, config["print_file"])

    #plotting and printing
    plot_fitness(plt_best_fitness, num_of_iterations)
    plot_average_fitness(plot_avg_fitness, num_of_iterations)
    print_best_chromosome(best_chromosome, config["print_file"])


    

    