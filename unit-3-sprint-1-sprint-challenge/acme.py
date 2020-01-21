"""
Module of classes for Acme Corporation.
"""

import random


class Product:
    """Class for any product sold by Acme Corporation."""

    def __init__(self, name, price=10, weight=20, flammability=0.5):
        self.name = name
        self.price = price
        self.weight = weight
        self.flammability = flammability
        self.identifier = random.randint(1000000, 9999999)

    def stealability(self):
        stealability = self.price / self.weight
        if stealability < 0.5:
            return "Not so stealable..."
        elif (stealability >= 0.5) & (stealability < 1.0):
            return "Kinda stealable."
        else:
            return "Very stealable!"

    def explode(self):
        explodability = self.flammability * self.weight
        if explodability < 10:
            return "...fizzle."
        elif (explodability >= 10) & (explodability < 50):
            return "...boom!"
        else:
            return "...BABOOM!!"


class BoxingGlove(Product):
    """Subclass of class Product that represents a boxing glove SKU."""

    def __init__(self, name, price=10, weight=10, flammability=0.5):
        super().__init__(name, price, weight, flammability)

    def explode(self):
        return "...it's a glove."

    def punch(self):
        if self.weight < 5:
            return "That tickles."
        elif (self.weight >= 5) & (self.weight < 15):
            return "Hey that hurt!"
        else:
            return "OUCH!"
