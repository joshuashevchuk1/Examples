
import numpy as np


def data_structures_example():
    # Tuple
    my_tuple = (1, 2, 3)

    # Dictionary
    my_dict = {'name': 'Alice', 'age': 30, 'city': 'New York'}

    # List
    my_list = ['apple', 'banana', 'cherry']

    # Print each structure
    print("Tuple:", my_tuple)
    print("Dictionary:", my_dict)
    print("List:", my_list)

    spaces = 100
    start = 0
    stop = 100
    elements = np.linspace(start,stop,spaces).tolist()

    # list comprehension to return the last ten of an array but only if len(elements) >= spaces
    numbered = [element for i, element in enumerate(elements) if element >= elements[len(elements)-10] and len(elements) >= spaces]

    print("numbered {}".format(numbered))

if __name__ == '__main__':
    data_structures_example()