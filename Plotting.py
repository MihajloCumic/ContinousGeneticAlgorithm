from matplotlib import pyplot as plt
import numpy as np

fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2)

def plot_fitness(best_fitnesses, num_of_iterations):
    x = np.linspace(0, num_of_iterations, num_of_iterations)
    
    ax1.plot(x[:len(best_fitnesses)], best_fitnesses)
    ax1.set_title("Najmanji trosak po generaciji")
    ax1.set_xlabel("Generacija")
    ax1.set_ylabel("Najmanji trosak")

    


def plot_average_fitness(avg_fintess, num_of_iterations):
    x = np.linspace(0, num_of_iterations, num_of_iterations)
    ax2.plot(x[:len(avg_fintess)], avg_fintess)
    ax2.set_title("Prosecan trosak po generaciji")
    ax2.set_xlabel("Generacija")
    ax2.set_ylabel("Prosecan trosak")

def show_plot():
    plt.show()
