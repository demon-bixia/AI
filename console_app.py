"""
a console app that runs all the algorithms
"""
from tree import arad
from console import print_solution
import dfs
import bfs
import ucs
import iddfs
import dls
import astar
import gbfs
import os

algorithms = {
    '1': dfs,
    '2': bfs,
    '3': ucs,
    '4': dls,
    '5': iddfs,
    '6': gbfs,
    '7': astar,
}


def main():
    os.system("clear")

    while True:
        try:
            algorithm_choice_text = "Select the a number of these algorithms:\n\
                    1. Depth first search\n\
                    2. Breadth first search\n\
                    3. Uniform cost search\n\
                    4. Depth limited search\n\
                    5. Iterative deepening depth first search\n\
                    6. Greedy best first searcg\n\
                    7. A* search\n\
                    8. exit\n"

            choice = input(algorithm_choice_text)

            os.system("clear")

            if choice == '8':
                break

            if choice == '4':
                limit = int(
                    input("enter the depth limit for depth limited search: "))

            algorithm = algorithms[choice]

            destination = "bucharest"

            try:
                if choice == '4':
                    solution = algorithm.find(arad, destination, limit)
                else:
                    solution = algorithm.find(arad, destination, limit)

                print("\n\n")
                print_solution(arad, solution)
                print("\n\n")

            except Exception as error:
                print(str(error))

        except:
            print("an error occured please try again")


if __name__ == "__main__":
    main()
