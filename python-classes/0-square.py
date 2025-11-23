#!/usr/bin/python3
"""
This module defines the Square class.
"""


class Square:
    """
    Represents a square with a private size attribute.
    """

    def __init__(self, size):
        """
        Initialize a square with a private size attribute.
        No type or value validation is performed.
        """
        self.__size = size
