import numpy as np

#returns the index of chosen chromosome
def parent_picker(cumulative_probability):
    rand_num = np.random.random()
    safety = 0
    for x in range(len(cumulative_probability)):
        safety = x
        if(x == 0):
            cp_prev = 0
        else:
            cp_prev = cumulative_probability[x-1]
        
            
        cp_curr = cumulative_probability[x]
        if(rand_num >= cp_prev and rand_num < cp_curr):
            return x  
    return safety

#selection equal chances
def equal_chances(kept_cnt):
    
    cumulative_probability = []

    for x in range(kept_cnt):
        cumulative_probability.append((x+1)/kept_cnt)
    
    return parent_picker(cumulative_probability)


#redklif crossing
def radcliffe(kept_cnt, new_population, mut_rate):

    cnt = kept_cnt

    while(cnt < len(new_population)):
        index_1 = equal_chances(kept_cnt)
        index_2 = equal_chances(kept_cnt)

        if(index_1 == index_2): continue

        parent1 = new_population[index_1]
        parent2 = new_population[index_2]

        beta = np.random.random()

        offspring = beta * parent1 + (1 - beta)*parent2
        mutation(offspring, mut_rate)

        new_population[cnt] = offspring

        cnt += 1

#normal mutation
def mutation(offspring, mut_rate):
    if(np.random.random() > mut_rate): return
    
    for x in range (len(offspring)):
        mu = 0
        sigma = 1

        gauss_rand = np.clip(np.random.normal(mu, sigma), -2, 2)
        
        offspring[x] = np.clip(offspring[x] + gauss_rand, -3, 3)
