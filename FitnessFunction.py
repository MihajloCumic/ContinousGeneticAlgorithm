import subprocess as sp
import numpy as np

def run_fitness(axis):
    args = list(axis.astype(str))
    fitness = bytes.decode(sp.check_output(['a'] + args))
    return float(fitness)

def fitness_function(population):
    return np.apply_along_axis(run_fitness, axis=1, arr=population)