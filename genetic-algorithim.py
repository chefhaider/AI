import random

pop_size = 100
genes = '''abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ 1234567890, .-;:_!"#%&/()=?@${[]}'''
target = "Charles Darwin"

class Gnome:

  def __init__(self,chromosome):
    self.chromosome = chromosome
    self.fitness = self.cal_fitness()

  
  def cal_fitness(self):

    global target
    fitness = 0


    for gene,target_g in zip(self.chromosome,target):
      if gene != target_g:
        fitness+=1

    return fitness


  @classmethod
  def mutated_gene(self):
    global genes
    return random.choice(genes)

  @classmethod
  def create_genome(self):
    
    global target

    return [ self.mutated_gene() for _ in range(len(target))]


  def mate(self,par2):

    child_chromosome = []
    for gp1, gp2 in zip(self.chromosome, par2.chromosome):
      prob = random.random()
      
      if prob < 0.45:
        child_chromosome.append(gp1)

      elif prob < 0.90:
        child_chromosome.append(gp2)

      else:
        child_chromosome.append(self.mutated_gene())
      
    return Gnome(child_chromosome)



              

def genetic_algorithim():
  population_size = 100
  generation = 1
  found = False

  population = []
  for _ in range(population_size):
    chromosome = Gnome.create_genome()
    population.append(Gnome(chromosome))

  while not found:
    population = sorted(population, key = lambda x:x.fitness)   

    if population[0].fitness <= 0:
      found = True
      print('found!')
      break
    
    new_generation = []
    
    size_ng = int((10*population_size)/100)
    new_generation.extend(population[:size_ng])

    size_ng = int((90*population_size)/100)
    for _ in range(size_ng):
      parent1 = random.choice(population[:50])
      parent2 = random.choice(population[:50])
      #print(parent2.chromosome,'x')
      child = parent1.mate(parent2)
      new_generation.append(child)

      population = new_generation


  return ''.join(population[0].chromosome)



genetic_algorithim()

    


