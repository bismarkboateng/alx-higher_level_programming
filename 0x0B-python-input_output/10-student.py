#!/usr/bin/python3
""" Module : 10-student """


class Student(object):
    """
        A student Class
    """
    def __init__(self, first_name, last_name, age):
        """ Initialize Student class """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
            Retrieve a dictionary representation of a Student
        """
        new_dict = {}
        if (attrs is not None):
            for i in attrs:
                if i in self.__dict__:
                    new_dict[i] = self.__dict__[i]
            return new_dict
        else:
            return self.__dict__
