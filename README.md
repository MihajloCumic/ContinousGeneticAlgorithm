# Continuous Genetic Algorithm

## Overview
This project involves fitting a neural network in the `g.c` file written in C++ using a continuous genetic algorithm implemented in Python. The continuous genetic algorithm is designed to optimize the neural network's performance by evolving a population of solutions over several generations.

## Technologies Used
- **Programming Language:** Python 3.11.2
- **Libraries:** 
  - `numpy` 1.24.2 
  - `matplotlib` 3.7.1
- **Compiler:** GCC for compiling the C++ code

## Program Instructions

### Compiling the C++ File
To compile the `g.c` file, use the following command:
```bash
gcc g.c -o a.exe
## Configuration

The configuration of the program is managed in the `config.json` file. The following parameters can be adjusted:

- `"chromosome_num"`: Number of chromosomes in the population.
- `"mut_rate"`: Mutation frequency during the genetic algorithm.
- `"num_of_iterations"`: Number of iterations or generations for each experiment.
- `"print_file"`: Path to the file where results will be saved.

## Running the Program

To run the program, use the command:

```bash
python main.py
```

## Genetic Algorithm Details

### Cost Function

The algorithm minimizes a predefined **cost function** that evaluates the performance of each chromosome (solution).

### Crossover Method

**Simple fusion (Radcliffe method)** is used for crossing chromosomes. This method ensures offspring remain within the limits of their parents.

### Mutation

Mutation is implemented using **dotted normal mutation** with a normal distribution.

- The mutation rate is set to 0.4 because the Radcliffe crossover method restricts offspring from exceeding the bounds of their parents, which may cause convergence to local minima. A higher mutation rate helps maintain diversity and avoid this issue.

### Selection

Selection is performed using a **uniform distribution** ("Equal chances").

- This method gives all chromosomes an equal chance of being selected, promoting a diverse population and reducing the risk of convergence to local minima.

### Threshold Cutoff

A threshold cutoff using the **median cost** is employed.

- This approach helps discard poorly adapted chromosomes, especially given the high mutation rate. It also avoids the need for sorting chromosomes.


