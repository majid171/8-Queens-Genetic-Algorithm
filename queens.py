import sys
import numpy as np
import random

NUMBER_OF_QUEENS = 8
MAX_FITNESS_SCORE = int((NUMBER_OF_QUEENS - 1)*(NUMBER_OF_QUEENS)/2)
POPULATION_SIZE = 20

def generate_board():
    initial_population = []

    for i in range(NUMBER_OF_QUEENS):
        initial_population.append(random.randint(0, NUMBER_OF_QUEENS - 1))
    
    return initial_population

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
    population = [generate_board() for i in range(POPULATION_SIZE)]
    return population

def can_stop(population):
    
    if MAX_FITNESS_SCORE in [fitness_function(pos) for pos in population]:
        return True
    
    return False

def cross_over(population):
    # Perform crossover here
    return generate_population()

def main():
    if len(sys.argv) != 1:
        print('ERROR')
        print('\tPlease run script as <py queens.py>')

    population = generate_population()

    while not can_stop(population):
        population = cross_over(population)

    for board in population:
        if fitness_function(board) == MAX_FITNESS_SCORE:
            print(board)

if __name__ == "__main__":
    main()