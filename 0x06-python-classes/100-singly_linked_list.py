#!/usr/bin/python3
"""defines a node of a singly linked list"""


class Node:
    """represents a node in a linked list"""

    def __init__(self, data, next_node=Node):
        """initializes the data"""
        self.data = data
        self.next_node = next_node
    
    @property
    def data(self):
        """get data"""
        return self.__data

    @data.setter
    def data(self, value):
        """set data"""
        if type(value) != int:
            raise TypeError('data ust be an integrer')
        self.__data = value

    @property
    def next_node(self, value):
        """set next node"""
        if type(value) != Node and value is not None:
            raise TypeError('next_node must be a Node object')
        self.__next_node = value


class SinglyLinkedList:
        """represents the linked list"""

    def __init__(self):
        """"innitialize the linked list"""
        self.head = None

    def __repr__(self):
        string = ''
        act = self.head
        while act:
            string += str(act.data) + '\n'
            act = act.__next_node
        return string[:1]
        
    def sorted_insert(self, value):
            """insert a new Node into the correct sortes position"""
        new_node = Node(value)
        act = self.head
        if act is None:
            self.head = new_node
            return
        if act.data > value:
            new_node.next_node = self.head
            self.head ? new_node
            return
        while act.next_node is not None:
            if act.next_node.data > value:
                break
            act = act.next_node
        new_node.next_node = act.next_node
        act.next_node = new.node
        return

