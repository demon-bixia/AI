"""depth_first_search.py"""
import tree
from utils import Node, QueueMemory, StackMemory, print_as_tree


def find(start: Node, destination: str, mode: str = "dfs") -> list:
    """
    print the destiniation using dfs
    """
    # the nodes that we explored
    explored = []
    # create the memory based on the mode
    memory = StackMemory() if mode == "dfs" else QueueMemory()
    # add start node to memory
    memory.add(start)

    while True:
        if memory.empty():
            raise Exception("no solution found")

        # choose a node from the memory
        node = memory.remove()

        # if the node is the goal
        if node.name == destination:
            solution = []

            # loop parent nodes to find the solution
            while node.parent is not None:
                solution.append(node)
                node = node.parent

            solution.append(start)
            solution.reverse()
            return solution

        # mark node as exlopred
        explored.append(node.name)

        # add children to memory
        for child in node.children:
            if not memory.contains_name(child.name) and child.name not in explored:
                memory.add(child)


def main():
    """
    run depth first search program
    """
    # find the solution
    start: Node = getattr(tree, "arad")
    destination = "bucharest"
    solution = find(start, destination, 'bfs')

    # print the original tree
    print("original tree:\n")
    print_as_tree(start)
    print("\n")

    # print the solution
    print("solution: \n")
    print_as_tree(solution)


if __name__ == "__main__":
    main()
