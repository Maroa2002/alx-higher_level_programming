#!/usr/bin/python3
"""
model: base
"""

import json


class Base:
    """Base  of all other classes in the project"""
    __nb_objects = 0

    def __init__(self, id=None):
        """constructor"""
        if id is not None:
            self.id = id
        else:
            self.__class__.__nb_objects += 1
            self.id = self.__class__.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation of list_dictionaries"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation json_string"""
        if json_string is None or len(json_string) == 0:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file"""
        if list_objs is None:
            list_objs = []
        json_list = [obj.to_dictionary() for obj in list_objs]
        filename = cls.__name__ + '.json'
        with open(filename, 'w', encoding='utf-8') as json_file:
            json_file.write(cls.to_json_string(json_list))

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set"""
        if cls.__name__ == "Rectangle":
            dummy_instance = cls(1, 1)
        if cls.__name__ == "Square":
            dummy_instance = cls(1)
        dummy_instance.update(**dictionary)
        return dummy_instance

    @classmethod
    def load_from_file(cls):
        """returns a list of instances"""
        filename = cls.__name__ + ".json"
        li = []
        try:
            with open(filename, 'r', encoding='utf-8') as file:
                instances = cls.from_json_string(file.read())
            for i, dic in enumerate(instances):
                li.append(cls.create(**instances[i]))
        except Exception:
            pass
        return li
