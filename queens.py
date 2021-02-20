import sys
import numpy as np
import random

NUMBER_OF_QUEENS = 8
MAX_FITNESS_SCORE = int((NUMBER_OF_QUEENS - 1)*(NUMBER_OF_QUEENS)/2)
POPULATION_SIZE = 2
MUTATION_RATE = 0.05
MAX_GENERATIONS = 1

class Board:
    def __init__(self):
        self.values = None
        self.fitness = None

def generate_board():
    board = []

    for i in range(NUMBER_OF_QUEENS):
        board.append(random.randint(0, NUMBER_OF_QUEENS - 1))
    
    return board

def fitness_function(board):
    score = MAX_FITNESS_SCORE

    # Checking up/down/left/right
    for i in range(len(board)):
        for j in range(i + 1, len(board)):
            if board[i] == board[j]:
                score -= 1
    
    # Checking diagonals
    for i in range(len(board)):
        for j in range(i, len(board)):
            if i != j:
                dx = abs(i - j)
                dy = abs(board[i] - board[j])
                if dx == dy:
                    score -= 1

    return score

def generate_population():

    population = [Board() for i in range(POPULATION_SIZE)]

    for board in population:
        board.values = generate_board()
        board.fitness = fitness_function(board.values)

    population.sort(key=lambda x: x.fitness)
    return population

def can_stop(population, generation):
    
    if MAX_FITNESS_SCORE in [pos.fitness for pos in population]:
        return True
    
    if generation > MAX_GENERATIONS:
        return True

    return False

def crossover(parent1, parent2):
    child = Board()

    child.values = parent1.values[:4]
    child.values += parent2.values[4:]

    child.fitness = fitness_function(child.values)
    return child


def mutate(board):
    if random.uniform(0, 1) < MUTATION_RATE:
        board.values[random.randint(0, NUMBER_OF_QUEENS - 1)] = random.randint(0, NUMBER_OF_QUEENS - 1)
        board.fitness = fitness_function(board.values)
    return board


def genetic_algorithm(population):
    newpopulation = []

    for i in range(len(population)):
	    print()

    return newpopulation

def main():
    if len(sys.argv) != 1:
        print('ERROR')
        print('\tPlease run script as <py queens.py>')

    population = generate_population()

    generation = 0

    while not can_stop(population, generation):
        population = genetic_algorithm(population)
        generation += 1

    print("Generation #:", generation, "\nSolutions:")

    for board in population:
        print(board.values, board.fitness)
        if board.fitness == MAX_FITNESS_SCORE:
            print(board.values)

if __name__ == "__main__":
    main()