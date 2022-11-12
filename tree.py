"""tree.py"""
from console import print_children_nodes_as_tree
from data_structures import Node

# super node
arad = Node("arad", cost=50, heuristic=366)

# arad children
sibiu = Node("sibiu", arad, 49, 253)

timisiara = Node("timisiara",  arad, 49, 329)

zerind = Node("zerind", arad, 49, 374)

# sibiu's children
fagaras = Node("fagaras", sibiu, 300, 178)

oradea = Node("oradea", sibiu, 30, 380)

rimnicu_vilcea = Node("rimnicu vilcea", sibiu, 50, 193)

# rimmcu vileea's children
craiova = Node("caraiova", rimnicu_vilcea, 40, 160)

pitesti = Node("pitesti", rimnicu_vilcea, 60, 98)

# fagaras's children
bucharest = Node("bucharest", fagaras, 30, 0)

# pitesti's children
bucharest = Node("bucharest", pitesti,  20, 0)

craiova = Node("caraiova", pitesti, 120, 160)


def main():
    """
    print the tree
    """
    print_children_nodes_as_tree(arad)


if __name__ == "__main__":
    main()
