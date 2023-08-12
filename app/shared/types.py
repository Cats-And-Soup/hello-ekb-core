from enum import Enum


class Roles(str, Enum):
    # admin = "admin"
    user = "user"
    manager = "manager"


class Rating(str, Enum):
    one = 1
    two = 2
    three = 3
    four = 4
    five = 5
