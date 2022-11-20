"""method that help in developing the console application"""
from typing import Union

from rich import print as rich_print
from rich.tree import Tree

from data_structures import Node


def build_tree(node: Node):
    """
    collect the children of the node in rich tree
    """
    # create the tree
    tree = Tree('Node Tree')

    # add the name of the node to the tree
    parent_tree = tree.add(
        f'{node.name} cost({node.cost}) heuristic({node.heuristic})')

    # check
    if node.has_children():
        for child in node.children:
            parent_tree.add(build_tree(child))

    return parent_tree


def build_solution_tree(node: Node, solution: list):
    """
    collect the children of the node in rich tree
    """
    # create the tree
    tree = Tree('Node Tree')

    # add the name of the node to the tree
    if node in solution:
        parent_tree = tree.add(
            f'[green]{node.name} [green]b({node.cost}) [green]h({node.heuristic})')
    else:
        parent_tree = tree.add(
            f'{node.name} b({node.cost}) h({node.heuristic})')

    # check
    if node.has_children():
        for child in node.children:
            parent_tree.add(build_solution_tree(child, solution))

    return parent_tree


def print_as_tree(printable: Union[list, Node]):
    """
    print a list or node as a tree
    """
    if isinstance(printable, list):
        print_list_as_tree(printable)
    elif isinstance(printable, Node):
        print_children_nodes_as_tree(printable)
    else:
        raise Exception("unprintable type")


def print_children_nodes_as_tree(node: Node):
    """
    print all the children of the node in tree format
    """
    tree = build_tree(node)

    # rich print the tree
    rich_print(tree)


def print_list_as_tree(node_list: list):
    """
    render a list of nodes as tree format
    """
    tree = Tree(f'[green]{node_list[0].name}')
    child_tree = tree

    # add rest of nodes
    for index, item in enumerate(node_list):
        if index > 0:
            child_tree = child_tree.add(
                f'[green]{item.name} b({item.cost}) h({item.heuristic})')

    rich_print(tree)


def print_solution(first_node: Node, solution: list):
    """
    highlight the correct path green
    """
    tree = build_solution_tree(first_node, solution)

    # rich print the tree
    rich_print(tree)
