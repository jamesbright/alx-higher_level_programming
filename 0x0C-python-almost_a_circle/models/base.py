#!/usr/bin/python3
""" Base class
"""
import json
import csv


class Base:
    """ base class with some methods
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """ Initialize class members
        """

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
    
    @staticmethod
    def to_json_string(list_dictionaries):
        """ returns the json string representation of
        list dictionary
        """

        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """Returns list of json string representation
        """

        if json_string is None or len(json_string) == 0:
            return "[]"
        else:
            return json.loads(json_string)

    def save_to_file(cls, list_objs):
        """Writes json representation of list objects
        to a file
        """

        with open(cls.__name__ + ".json", mode="w") as write_file:
            
            if list_objs is None:
                write_file.write("[]")
            else:
                write_file.write(cls.to_json_string(
                    [item.to_dictionary() for item in list_objs]))

    def create(cls, **dictionary):
        """Returns an instance with all attributes already set
        """
        
        if cls.__name__ == "Rectangle":
            temp = cls(1, 1)
        if cls.__name__ == "Square":
            temp = cls(1)

        temp.update(**dictionary)
        return temp


    def load_from_file(cls):
        """Returns a list of instances in a file
        """
        
        res = []
        with open(cls.__name__ + ".json", mode="r") as read_file:
            text = read_file.read()
            text = cls.from_json_string(text)
            for item in text:
                if type(item) == dict:
                    res.append(cls.create(**item))
                else:
                    res.append(item)
        return res

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Serializes in csv
        """

        res = [item.to_dictionary() for item in list_objs]
        with open(cls.__name__ + ".csv", mode="w") as save_file:
            write_to = csv.DictWriter(save_file, res[0].keys())
            write_to.writeheader()
            write_to.writerows(res)

    @classmethod
    def load_from_csv(cls):
        """Deserializes in csv
        """

        res = []
        res_dict = {}
        with open(cls.__name__ + ".csv", mode="r") as read_file:
            read_from = csv.DictReader(read_file)
            for item in read_from:
                for k, v in dict(item).items():
                    res_dict[k] = int(v)

                    res.append(cls.create(**res_dict))
        return res
