"""tree.py"""
from utils import Node, print_children_nodes_as_tree

# super node
arad = Node("arad")

# arad children
sibiu = Node("sibiu", parent=arad)

timisiara = Node("timisiara", parent=arad)

zerind = Node("zerind", parent=arad)

# sibiu's children
fagaras = Node("fagaras", parent=sibiu)

oradea = Node("oradea", parent=sibiu)

rimmcu_vileea = Node("rimmcu_vileea", parent=sibiu)

# rimmcu vileea's children
craiova = Node("caraiova", parent=rimmcu_vileea)

pitesti = Node("pitesti", parent=rimmcu_vileea)

# fagaras's children
bucharest = Node("bucharest", parent=fagaras)

# pitesti's children
bucharest = Node("bucharest", parent=pitesti)

craiova = Node("caraiova", parent=pitesti)


def main():
    """
    print the tree
    """
    print_children_nodes_as_tree(arad)


if __name__ == "__main__":
    main()
