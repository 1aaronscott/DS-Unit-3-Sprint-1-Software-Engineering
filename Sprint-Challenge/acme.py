"""
Class for the products produced by Acme Corportation.
"""
from random import randint


class Product:
    """Product class parameters:
    name(=None)
    price(=10)
    weight(=20)
    flammability(=0.5)
    Methods:
    stealability (Determines likelihood of product theft.)
    explode (Likelihood the product will explode)
    """

    def __init__(self, name=None, price=10, weight=20, flammability=0.5,
                 identifier=randint(1000000, 10000000)):
        self.name = name
        self.price = price
        self.weight = weight
        self.flammability = flammability
        self.identifier = identifier

    def stealability(self):
        """Determines likelihood of product theft."""
        self.stealable = self.price/self.weight
        # print (self.price, self.weight, self.stealable)
        if self.stealable < 0.5:
            print("Not so stealable...")
        elif self.stealable >= .5 and self.stealable < 1.0:
            return("Kinda stealable.")
        else:
            return("Very stealable!")

    def explode(self):
        """Likelihood the product will explode"""
        self.expl = self.weight*self.flammability
        # print(self.expl)
        if self.expl < 10:
            return("...fizzle")
        elif self.expl >= 10 or self.expl < 50:
            return("...boom!")
        else:
            return("...BABOOM!!")


class BoxingGlove(Product):
    """A special specific thing which adds punch!"""
    weight = 10

    def __init__(self, name=None, price=10, weight=10, flammability=0.5, identifier=randint(1000000, 10000000)):
        super().__init__(name=name, price=price, weight=weight,
                         flammability=flammability, identifier=identifier)

    def explode(self):
        """Gloves don't explode"""
        return("...it's a glove.")

    def punch(self, weight=10):
        """How hard is that punch?"""
        if self.weight < 5:
            return("That tickles.")
        elif self.weight >= 5 or self.weight < 15:
            return("Hey that hurt!")
        else:
            return("OUCH!")
