#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Creating a chained list class
"""

__author__ = 'Mohamed Ouertani'

class Node:

    """Structuring Node Class"""

    def __init__(self, value:float):
        self.value = value
        self.next = None

    def __str__(self):

        string = str(self.value)
        if self.next is not None:
            string += ", " + str(self.next)
        return string

    def get_node_value(self):
        """Gets node value"""
        return self.value

    def set_node_value(self,value:float):
        """Sets new node value"""
        self.value = value



class ChainedList:

    """Structuring ChaindeList Class"""

    def __init__(self):

        self.first_node = None

    def __getitem__(self, key:int):

        index = 0
        node = self.first_node
        while index < key and node is not None:
            index += 1
            node = node.next
        if node is None:
            return "index out of range"
        return  node.value

    def add_node(self, value:float):

        """Adds a node to the chained list object"""

        if self.first_node is None:
            self.first_node = Node(value)
        elif value < self.first_node.value:
            node = Node(value)
            node.next = self.first_node
            self.first_node = node
        else:
            node = Node(value)
            cl_node = self.first_node.next
            node.next = self.first_node
            while cl_node is not None and node.value > cl_node.value:
                node.next = cl_node
                cl_node = cl_node.next
            prev_node = node.next
            prev_node.next = node
            node.next = cl_node

    def remove_node(self,value:float):

        """Removes node value from chained list"""

        node = self.first_node
        prev_node = None
        if node is None or value < node.value:
            return print(f"Value {value} is not in chained list")
        while node is not None and value > node.value :
            prev_node = node
            node = node.next
        if node is None:
            return print(f"Value {value} is not in chained list")
        while node is not None and node.value == value:
            if prev_node is None:
                self.first_node = self.first_node.next
                node = self.first_node
            else:
                prev_node.next = node.next
                node = node.next

    def length(self):

        """Calculates number of nodes in chained list"""

        list_length = 0
        node = self.first_node
        if  node is None:
            return "This chained list is empty"
        list_length += 1
        while node.next is not None:
            list_length += 1
            node = node.next
        return list_length

    def __str__(self):

        if self.first_node is None:
            return "liste vide"
        return str(self.first_node)
