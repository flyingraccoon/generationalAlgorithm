import random,operator
target = 'hello'
letters = 'abcdefghijklmnopqrstuvwxyz 1234567890'
listLetters = list(letters)
class Player():
    def __init__(self,target,letters,chromosome,total,listLetters):
        self.target = target
        self.letters = letters
        self.chromosome = chromosome
        self.total = total
        self.listLetters = listLetters
        self.listChromosome = listChromosome

    def generate():
        global listLetters
        chromosome = []
        for x in range(len(target)):
            randomInt = random.randint(0,len(listLetters)-1)
            chromosome.append(listLetters[randomInt])
        return chromosome


    def fitness(target,chromosome):
        total = 0
        for x in zip(target,chromosome):
            if x[0] == x[1]:
                total+=1
        return total

    def mutate(chromosome):
        chromosome[random.randint(0,len(chromosome)-1)] = listLetters[random.randint(0,len(listLetters)-1)]
        return chromosome

    def best(parents):
        sortedParents = sorted(parents,key=lambda x: x[1], reverse = True)
        return sortedParents
