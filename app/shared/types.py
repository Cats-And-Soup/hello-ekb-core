from enum import Enum


class Roles(str, Enum):
    # admin = "admin"
    user = "user"
    manager = "manager"


class Rating(int, Enum):
    one = 1
    two = 2
    three = 3
    four = 4
    five = 5
    six = 6
    seven = 7
    eight = 8
    nine = 9
    ten = 10
