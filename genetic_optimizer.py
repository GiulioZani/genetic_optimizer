import numpy as np


def optimize(
    get_random_genome,
    get_offspring,
    get_fitness, # genome -> fitness
    pop_size=100,
    generations=60,
    best_threshold = 0.3,
):
    best_count = int(np.floor(best_threshold * pop_size))
    genomes = np.array([get_random_genome() for _ in range(pop_size)])
    for gen_n in range(generations):
        fitnesses = list(map(get_fitness, genomes))
        best_idxs = np.argsort(fitnesses)[:best_count]
        best_genomes = genomes[best_idxs]
        offspring = [
            get_offspring(best_genomes[i], best_genomes[j]) \
            for i, j in get_random_couples(len(best_genomes))
        ]
        genomes = np.concatenate((
            best_genomes,
            offspring,
            [get_random_genome() for _ in range(pop_size - 2*best_idxs)]
        ))
        print(f"Best fitness: {fitnesses[best_idxs[0]]}")

    best_idx = np.argmax(list(map(get_fitness, genomes)))
    return genomes[best_idx]


def get_random_couples(size):
    couples = set()
    offspring = []
    for i in range(size):
        j = i
        while j == i or (j, i) in couples:
            j = np.random.randint(0, size)
        couples.add((i, j))
    return couples
