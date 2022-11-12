"""helpful methods"""
from data_structures import Node


def find_solution(start: Node, node: Node) -> list:
    """
    calculate the solution from the given node
    """
    solution = []

    # loop parent nodes to find the solution
    while node.parent is not None:
        solution.append(node)
        node = node.parent

    solution.append(start)
    solution.reverse()
    return solution
