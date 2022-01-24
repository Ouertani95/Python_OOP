#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Main file for testing the chained list class
"""

from chained_list_class import ChainedList

__author__ = 'Mohamed Ouertani'

# Testing code :

def testing_function():

    """Test add, remove and length methods on predifined chained list"""

    test_list = [0,5,4,9,15,2,4,16,18,1,1,-1,-3,6]
    chained_list = ChainedList()
    for i in test_list:
        chained_list.add_node(i)
    print(chained_list)
    print("Initial chained list length is : " + str(chained_list.length()) + "\n")

    #Adding values
    adding_list = [7,20,-20]
    for i in adding_list:
        chained_list.add_node(i)
        print(chained_list)
        print(f"Added value : {i}")
        #Length method
        print("New length is : " + str(chained_list.length()) + "\n")

    #Removing values
    removing_list = [1,18,-20,20]
    for i in removing_list:
        chained_list.remove_node(i)
        print(chained_list)
        print(f"Removed value : {i}")
        print("New length is : " + str(chained_list.length()) + "\n")

    #ChainedList node values can also be accessed with index thanks to __getitem__ method
    print("First node value : " + str(chained_list[0]))
    list_length = chained_list.length()
    print("Last node value : " + str(chained_list[list_length-1]))


if __name__ == "__main__" :
    testing_function()
