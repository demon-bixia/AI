"""iterative deepening depth first search"""
import tree
from console import print_as_tree
from data_structures import Node
from utils import find_solution
from typing import Union


def depth_limited_search(start: Node, destination: str, max_depth: int):
    """
    preform depth limited search from a given start
    """
    # record the last node reached to
    # check if we reached the end of the array
    last_node_reached = start

    # if the node is the solution calculate path taken
    if start.name == destination:
        return (start, last_node_reached)

    # If reached the maximum depth, stop recursing.
    if max_depth <= 0:
        return (None, last_node_reached)

    # recur for all the children of this node
    for child in start.children:
        found_node, last_node_reached = depth_limited_search(
            child, destination, max_depth - 1)

        if found_node:
            return (found_node, last_node_reached)
        else:
            return (None, last_node_reached)


def find(start: Node, destination: str) -> list:
    """
    print the destiniation using iddfs
    using recursion
    """
    previous_last_node_reached = None

    # Repeatedly depth-limit search till the maximum depth
    index = 0

    while True:
        found_node, last_node_reached = depth_limited_search(
            start, destination, index)

        if found_node:
            return find_solution(start, found_node)

        print("not found at depth: ", index)

        if last_node_reached == previous_last_node_reached:
            raise Exception("no solution found")

        previous_last_node_reached = last_node_reached

        index += 1


def main():
    """
    run iddfs program
    """
    # find the solution
    start: Node = getattr(tree, "arad")
    destination = "bucharest"
    solution = find(start, destination)

    # print the original tree
    print("original tree:\n")
    print_as_tree(start)
    print("\n")

    # print the solution
    print("solution: \n")
    print_as_tree(solution)


if __name__ == "__main__":
    main()
