"""data structures that help in developing the algorithms"""


class Node:
    """
    represents a node of a tree
    """

    def __init__(self, name, parent=None, cost=None, heuristic=None):
        self.name = name  # name of the node
        self.parent = parent  # the node before this node

        self.cost = cost  # cost to arrive at node from parent node
        self.heuristic = heuristic  # the heuristic value for this node

        self.path_cost = None  # the total cost of the path from starting node to this node
        self.children = []  # list of nodes that come after this node

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

    def add(self, node: Node):
        """
        add node to memory
        """
        self.memory.append(node)

    def contains_name(self, name: str):
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


class LowCostMemory(Memory):
    """
    the memory uniform cost search uses
    """

    def add(self, node: Node) -> None:
        """
        everytime you add a node calculate the cost of full path to this node.
        """
        node.path_cost = self.calculate_cost(node)
        self.memory.append(node)

    def remove(self) -> Node:
        """
        remove node from memory based on the lowest total path cost
        """
        if self.empty():
            raise Exception("empty memory")
        else:
            minimum_cost_node, node_index = self.get_minimum_cost_node()

            # remove the node from the memory
            self.memory.pop(node_index)

            return minimum_cost_node

    def calculate_cost(self, node: Node):
        """
        calculate the cost of full path to this node.
        """
        current_node = node
        total_cost = 0

        while current_node.parent is not None:
            total_cost += current_node.cost
            current_node = current_node.parent

        return total_cost

    def get_minimum_cost_node(self):
        """
        get the node that costs the least in memory
        """
        minimum_cost_node = self.memory[0]
        minimum_cost_node_index = 0

        for index, node in enumerate(self.memory):
            if node.path_cost < minimum_cost_node.path_cost:
                minimum_cost_node = node
                minimum_cost_node_index = index

        return (minimum_cost_node, minimum_cost_node_index)


class QueueMemory(Memory):
    """
    Memory used by greedy best first algorithm
    """

    def remove(self):
        """
        remove the item with the best heuristic value
        """
        if self.empty():
            raise Exception("empty memory")
        else:
            best_node, node_index = self.get_node_based_on_heuristic()

            # remove the node from the memory
            self.memory.pop(node_index)

            return best_node

    def get_node_based_on_heuristic(self):
        """
        return the node with best heuristic value
        """
        best_node = self.memory[0]
        best_node_index = 0

        for index, node in enumerate(self.memory):
            if node.heuristic > best_node.heuristic:
                best_node = node
                best_node_index = index

        return (best_node, best_node_index)
