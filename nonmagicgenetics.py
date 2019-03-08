import random,time
from player import *

generation = 1000
parentFitnesses = []

start = time.time()
def main():
    while True:
        for x in range(generation):
            parent = Player.generate()
            #print(parent)
            #time.sleep(2)
            parentFitnesses.append((parent,Player.fitness(target,parent)))
        bestParent = Player.best(parentFitnesses)
        bestparentChromosome = bestParent[0][0]
        for letter in zip(bestparentChromosome,target):
            print(letter)
        break
    print(bestParent[0])
if __name__ == '__main__':
    main()
