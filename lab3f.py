#!/usr/bin/env python3
#usernam-rbhandari17@myseneca.ca
# Create the list my_list here
from lab3f import *

my_list = [1, 2, 3, 4, 5]

def add_item_to_list(ordered_list):
    # Appends new item to end of list with the value (last item + 1)
    ordered_list.append(ordered_list[-1] + 1)

def remove_items_from_list(ordered_list, items_to_remove):
    # Removes all values found in items_to_remove list from ordered_list
    for item in items_to_remove:
        if item in ordered_list:
            ordered_list.remove(item)

# Main code
if __name__ == '__main__':
    print(my_list)  # Initial list
    add_item_to_list(my_list)  # Add item to the list
    add_item_to_list(my_list)  # Add item to the list
    add_item_to_list(my_list)  # Add item to the list
    print(my_list)  # List after adding items
