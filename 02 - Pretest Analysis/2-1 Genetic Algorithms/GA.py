import numpy as np
import bisect

class GeneticAlgorithm:
    def __init__(self,minVal,maxVal, mutateProb, population_create, fitness_fn):
        self.population = population_create()
        self.fitness_fn = fitness_fn
        self.mutateProb = mutateProb
        self.generation = 0
        self.bestDna = ""
        self.converged = 0
        self.minVal = minVal
        self.maxVal = maxVal

    def RandomSelection(self):
        fitness = map(self.fitness_fn,self.population)
        totals = []
        for w in fitness:
            totals.append(totals[-1]+w if totals else w)
        idx = bisect.bisect(totals,np.random.uniform(0,totals[-1]))
        
        return self.population[idx]

    def Mutate(self,child):
        if np.random.uniform(0, 1) >= float(self.mutateProb)/100.0:
            return child
        n = np.random.randint(0,len(child))
        m = np.random.randint(self.minVal,self.maxVal)
        xm = child[:n] + str(m) + child[n+1:]
        return xm
    
    def Reproduce(self,parent1, parent2):
        n = np.random.randint(0,len(parent1))
        child1 = parent1[:n] + parent2[n:]
        child2 = parent2[:n] + parent1[n:]
        return (child1,child2)

    def GetBest(self):
        maxIdx = 0
        maxW = 0
        for i in range(0,len(self.population)):
            w = self.fitness_fn(self.population[i])
            if w > maxW:
                maxIdx = i
                maxW = w
        return self.population[maxIdx],maxW

    def NextGeneration(self):
        new_population = []
        for i in range(0,int(len(self.population)/2)):
            x = self.RandomSelection()
            y = self.RandomSelection()
            child1,child2 = self.Reproduce(x,y)
            child1 = self.Mutate(child1)
            child2 = self.Mutate(child2)
            new_population.append(child1)
            new_population.append(child2)
        self.population=new_population
        self.generation += 1
        self.bestDna,self.converged = self.GetBest()