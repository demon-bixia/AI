"""iterative deepening depth first search"""
import tree
from console import print_as_tree
from data_structures import Node
from utils import find_solution


def depth_limited_search(start: Node, destination: str, max_depth: int):
    """
    preform depth limited search from a given start
    """

    # if the node is the solution calculate path taken
    if start.name == destination:
        return start

    # If reached the maximum depth, stop recursing.
    if max_depth <= 0:
        return None

    # recur for all the children of this node
    for child in start.children:
        found_node = depth_limited_search(child, destination, max_depth - 1)
        if found_node:
            return found_node


def find(start: Node, destination: str, max_depth: int) -> list:
    """
    print the destiniation using iddfs
    using recursion
    """

    # Repeatedly depth-limit search till the maximum depth
    for index in range(max_depth):
        found_node = depth_limited_search(start, destination, index)
        if found_node:
            return find_solution(start, found_node)

    # if this line is reached it means the loop is over and
    # no solution is returned
    raise Exception("no solution found")


def main():
    """
    run iddfs program
    """
    # find the solution
    start: Node = getattr(tree, "arad")
    destination = "bucharest"
    solution = find(start, destination, 5)

    # print the original tree
    print("original tree:\n")
    print_as_tree(start)
    print("\n")

    # print the solution
    print("solution: \n")
    print_as_tree(solution)


if __name__ == "__main__":
    main()
