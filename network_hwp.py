from itertools import permutations


def draw_network(getdata):
    word_combinations = list(permutations(getdata, 2))
    print(word_combinations)
