#!/usr/bin/python3
"""
 adds all arguments to a Python list,
 and then save them to a file
"""


import sys
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

# excluding the script name
arguments = sys.argv[1:]

# loading existing data from JSON file or creates an empty if doesnt exist
try:
    existing_data = load_from_json_file("add_item.json")
except Exception:
    existing_data = []

# adding the command line arguments to the list
existing_data.extend(arguments)

# saving the list to JSON file
save_to_json_file(existing_data, "add_item.json")
