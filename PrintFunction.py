import os

def print_results(best_fitness, avg_fitness,iteration = None, print_file = None):
    start_flag = False
    if(iteration == None): start_flag = True
    if(print_file != None and os.path.isfile(print_file)):
            file = open(print_file, "a")
            if(start_flag):
                 file.write("\n**************Start***************\n")
                 file.write(f"Starting population -> least cost: {best_fitness}, average cost: {avg_fitness}\n")
            else:
                file.write(f"Iteration: {iteration}, least cost: {best_fitness}, average cost: {avg_fitness}\n")
            file.close()
    else:
        print("Iteration:" + str(iteration))
        print("\tleast cost:" + str(best_fitness))
        print("\taverage cost:" + str(avg_fitness))

def print_best_chromosome(best_chromosome, print_file = None):
    
    if(print_file != None and os.path.isfile(print_file)):
            file = open(print_file, "a")
            file.write(f"Chromosome with least cost -> {best_chromosome}\n")
            file.close()
    else:
        print(f"Chromosome with least cost -> {best_chromosome}\n")


