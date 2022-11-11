"""utils.py"""
from typing import Union

from rich import print as rich_print
from rich.tree import Tree


class Node:
    """
    represents a node of a tree
    """

    def __init__(self, name, parent=None):
        self.name = name
        self.parent = parent
        self.children = []

        if self.parent:
            parent.children.append(self)

    def has_children(self):
        """
        check if the node has children
        """
        return len(self.children) > 0


class Memory:
    """
    memory that contains the decision nodes
    """

    def __init__(self):
        self.memory = []

    def add(self, node):
        """
        add node to memory
        """
        self.memory.append(node)

    def contains_name(self, name):
        """
        check if node is in memory using name
        """
        return any(node.name == name for node in self.memory)

    def empty(self):
        """
        check if memory is empty
        """
        return len(self.memory) == 0


class StackMemory(Memory):
    """
    the stack depth first search uses
    """

    def remove(self):
        """
        remove last node from memory
        """
        if self.empty():
            raise Exception("empty memory")
        else:
            node = self.memory[-1]  # get last item in fronter
            # slice the list and remove the last item
            self.memory = self.memory[:-1]
            return node


class QueueMemory(Memory):
    """
    the queue breadth first search uses
    """

    def remove(self):
        """
        remove first node from memory
        """
        if self.empty():
            raise Exception("empty memory")
        else:
            node = self.memory[0]  # get the first item from memory
            # slice the list and remove the first item
            self.memory = self.memory[1:]
            return node


# printing of trees

def build_tree(node: Node):
    """
    collect the children of the node in rich tree
    """
    # create the tree
    tree = Tree('Node Tree')

    # add the name of the node to the tree
    parent_tree = tree.add(node.name)

    # check
    if node.has_children():
        for child in node.children:
            parent_tree.add(build_tree(child))

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
            child_tree = child_tree.add(f'[green]{item.name}')

    rich_print(tree)
