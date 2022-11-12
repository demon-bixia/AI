"""tree.py"""
from console import print_children_nodes_as_tree
from data_structures import Node

# super node
arad = Node("arad", cost=50, heuristic=366)

# arad children
sibiu = Node("sibiu", arad, 140, 253)

timisoara = Node("timisiara",  arad, 118, 329)

zerind = Node("zerind", arad, 75, 374)

# sibiu's children
fagaras = Node("fagaras", sibiu, 99, 178)

oradea = Node("oradea", sibiu, 71, 380)

rimnicu_vilcea = Node("rimnicu vilcea", sibiu, 80, 193)

# rimmcu vileea's children
craiova = Node("caraiova", rimnicu_vilcea, 146, 160)

pitesti = Node("pitesti", rimnicu_vilcea, 97, 98)

# fagaras's children
bucharest = Node("bucharest", fagaras, 211, 0)

# pitesti's children
bucharest = Node("bucharest", pitesti,  101, 0)

craiova = Node("caraiova", pitesti, 138, 160)


def main():
    """
    print the tree
    """
    print_children_nodes_as_tree(arad)


if __name__ == "__main__":
    main()
