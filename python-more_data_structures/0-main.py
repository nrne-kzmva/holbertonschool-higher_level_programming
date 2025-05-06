#!/usr/bin/python3
safe_print_list = __import__('0-safe_print_list').safe_print_list
my_list = [1, 2, 3, 4, 5]
# Test 1:
nb_print = safe_print_list(my_list, 2)
print("nb_print: {:d}".format(nb_print))
# Test 2:
nb_print = safe_print_list(my_list, len(my_list))
print("nb_print: {:d}".format(nb_print))
# Test 3:
nb_print = safe_print_list(my_list, len(my_list) + 2)
print("nb_print: {:d}".format(nb_print))
