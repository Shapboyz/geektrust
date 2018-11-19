from Set2Problem1.battlian import Battlian

class Region():
    """ Class to repersent a Region be it lengburu, or falicornia.

    Attributes:
        n(object) - n number of dynamic Attributes(variables) objects of class
                    Battlian.
    Methods:
        deployBattlian - to counter the attacking Battlian
        borrowFromOtherBattlian - to borrow from other Battlian of lengburu.

    """

    def __init__(self, name, kwargs):
        """ Create instance with given name and dict of key value pair.
            name is to set the __name__ of instance.
            and dict for creating instance of Battlian for self instance.
            where k denotes the name of Battlian and v is size or number of
            elements in Battlian.

            Args:
                Param1(str) : name - to set __name__.
                Param2(dict) : kwargs - size of battlian.
        """
        self.__name__ = name
        self.__dict__.update( (k, Battlian(size = v))
            for k, v in kwargs.items())

    def __str__(self):
        """ To repersent class object in string format. Only for the instance
            of Battlian and not any other Attributes.
        """
        items = {key: str(item.size) for key, item in vars(self).items()
            if isinstance(item, Battlian)}
        return "{}".format(items)

    def deployBattlian(self, other, battlian):
        """ Takes two instance of Region, self and other and name of the
            Battlian to be deployed.
            return the diff of size of battlian instance of defence and attack.
            Args:
                Param1(object) : other - instance of Battlian.
                Param2(object) : str - name of Battlian.
            Returns:
                Param1(int): diff of size in int.
        """
        if(getattr(self, battlian, None)):
            return (getattr(self, battlian) - getattr(other, battlian))

    def borrowFromOtherBattlian(self, currBatt, prevBatt=None, nextBatt=None):
        """ Check if for current battlian, other battlians can be borrowed,
            if yes update the new strength or size of current as well as the
            one borrowed from.
            As per login, First borrow is taken from lower ranks and then
            higher if possible.

            Here lower means (Horse for Elephent and so on).
            Here higher means (Elephent for Horse and so on).

            Args:
                Param1(str) : currBatt - name of current Battlian.
                Param2(str) : prevBatt - name of prev(lower) Battlian.
                Param3(str) : nextBatt - name of next(higher) Battlian.

        """
        if prevBatt and getattr(self, prevBatt, None):
            getattr(self, currBatt).borrowFromLowerBatt(
                getattr(self, prevBatt)
            )
        if nextBatt and getattr(self, nextBatt, None):
            getattr(self, currBatt).borrowFromHigherBatt(
                getattr(self, nextBatt)
            )
        return
