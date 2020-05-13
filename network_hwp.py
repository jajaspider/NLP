from itertools import permutations
import networkx as nx
from networkx.drawing.nx_pydot import to_pydot
from IPython.core.display import Image


def get_combination(getdata):
    word_combinations = list(permutations(getdata, 2))
    print(word_combinations)
    return word_combinations


def draw_network(data1, data2):
    print("-")
