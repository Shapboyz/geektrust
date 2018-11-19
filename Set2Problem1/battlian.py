from math import ceil

class Battlian():
    """A Battlian consisting of the size(number of troops) in int.

    Attributes:
        size: A int to set the Strength of Battlian.
    """

    def __init__(self, size=0):
        """Return a Battlian instance with size(number) of troops."""
        self.size = size

    def __str__(self):
        """
            To repersent class object in string format.
        """
        return "size : {}".format(self.size)

    def __sub__(self, other):
        """ Operator Overloading of __sub__ method.
            Takes self and other instance of battlian and update the self
            instance size accordingly.
            Args:
                Param1(object) : other - instance of Battlian class.
        """
        self.size = self.size - ceil(other.size/2)
        return

    def borrowFromLowerBatt(self, lower):
        """ Takes self and lower instance of battlian and update the self and
            lower instances size accordingly.
            check how many lower troops can be borrowed till self is below zero
            and lower have twice unit per single unit of self to give.

            Args:
                Param1(object) : lower - instance of Battlian class.
        """
        while lower.size>=2 and self.size < 0:
            lower.size -= 2
            self.size += 1
        return

    def borrowFromHigherBatt(self, higher):
        """ Takes self and higher instance of battlian and update the self and
            higher instances size accordingly.
            check how many higer troops can be borrowed till self is below zero
            and higer have one unit for two unit of self to give.

            Args:
                Param1(object) : higher - instance of Battlian class.
        """
        while higher.size>0 and self.size<0:
            higher.size -= 1
            self.size += 2
        if self.size>0:
            self.size=0
        return
