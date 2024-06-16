# continuous-genetic-algorithm
## Fitting a neural network in g.c file written in C++ with a continuous genetic algorithm written in Python.
## Technologies
* Language: Python 3.11.2
* Libraries: numpy 1.24.2, matplotlib 3.7.1
## Program
* Compiling the g.c file is done with command:
   ```console
   gcc g.c -o a.exe
   ```
* Configuration of the program is in **config.json** file, following parameters can be set:
   * *"chromosome_num"* -number of chromosomes
   *  *"mut_rate"* -frequency of mutation
   *  *"num_of_iterations"* -number of iteration of one experiment
   *  *"print_file"* - path to a file where results will be printed
* Running the program is done with the command:
   ```console
   python main.py
   ```
## About the genetic algorithm
* ### **Cost function** was used.
* ### **Crossing** was done wiht the method of simple fusion, Radcliffe.
* ### **Mutation** was done with dotted normal mutation, normal distribution.
   * Frequency of the mutation is set to 0.4 because Radcliffe method of crossing does not allow for offspring to go beyond the limits of their parents, because of that function would converge to some local minimum and that is why the mutation frequency must be higher.
* ### **Selection** was implemented with uniform distribution, "Equal chances".
   * With the high frequency of mutation and the uniform selection a more diverse population is produced which avoids local minimums, because the selection using the uniform distribution does not give priority to the chromosomes with the least cost and thus we get more diverse offspring and it also prevents the median from getting too close to the least cost because this would quickly reduce the number of selected chromosomes for mating.
* ### Threshold **cutoff** with the medias as a threshold is used.
   * because the average cost would leave too many poorly adapted chromosomes due to the high mutation frequency. Also this method does not require chromosome sorting.
## Experiment results
  * ### running the algorithm with 10 chromosomes for 10 generations
     first graphic shows the least cost per generation and second one shows the average cost per generation
    ![Grafik_10_hromozoma](https://github.com/cumicm/continuous-genetic-algorithm/assets/126609170/c67565c4-415c-4532-a39f-c95d19632053)
  * ### running the algorithm with 50 chromosomes for 50
    ![Grafik_50_hromozoma](https://github.com/cumicm/continuous-genetic-algorithm/assets/126609170/00b6f9be-477e-4af0-8238-92901fd236d5)
  * ### running the algorithm with 90 chromosomes
    ![Grafik_90_hromozoma](https://github.com/cumicm/continuous-genetic-algorithm/assets/126609170/43129f13-74de-4c2f-8f97-d4f2aaf7dbf7)


