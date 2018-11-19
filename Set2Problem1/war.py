from Set2Problem1.region import Region
from Set2Problem1.battlian import Battlian
from copy import deepcopy

def createRegion(name="Temp", userInput=None):
    """ To create object of Region, if userinput is provided its based on Input
        else its default for lengburu.

        Args:
            Param1(list) : userInput - [value, key, ...] pair of user input

        Returns:
            Param1(object or False) : if object is created successfully
                return object else return False
    """

    if userInput and len(userInput)%2==0:
        kwargsItems = {}
        for i in range(0,len(userInput),2):
            kwargsItems[userInput[i+1]] = int(userInput[i])
    elif userInput:
        return False
    else:
        #default lengburu army
        kwargsItems = {'H':100, 'E':50, 'AT':10, 'SG':5}
    return Region(name, kwargsItems)


def compareArmyStrength(defence, attack):
    """ Function take defence(lengburu) and attack(falicornia) instance of
        Region as input and returns the lengburu deployment of battlians.

        Functionality:
            First it checks for how much of the current Battlian needs to be
        deployed to counter attacking battlian. Using deployBattlian method.

        If it can be countered it moves to checkc next battlian, else it tries
        to borrow from other available battlians that is taken care by
        borrowFromOtherBattlian method.

        Args:
            Param1(object) : defence - instance of Region.
            Param2(object) : attack - instance of Region.

    """

    attackBattlian = [x for x in vars(attack) if isinstance(
        getattr(attack, x, None), Battlian)]
    countBattlian = len(attackBattlian)
    solution = deepcopy(defence)

    for idx, val in enumerate(attackBattlian):
        if not getattr(solution, val, None):
            setattr(solution, val, Battlian(size=0))

        solution.deployBattlian(attack, val)
        if getattr(solution, val, None) and getattr(solution, val).size < 0:
            solution.borrowFromOtherBattlian(val,
                None if idx==0 else attackBattlian[idx-1],
                None if idx==countBattlian-1 else attackBattlian[idx+1])

    return outputResult(defence, solution) #show output in required format


def outputResult(defence, solution):
    """ To prettify the output, and check if lengburu wins or loses.
        if solution instance have any battlian with negative size, lengburu
        loses to falicornia.

        Args:
            Param1(object) : defence - instance of Region.
            Param2(object) : solution - instance of Region.
    """

    outputList = []
    gameStatus = "wins"

    for attr in vars(solution):
        if isinstance(getattr(solution, attr, None), Battlian):
            if getattr(solution, attr).size < 0:
                gameStatus = "loses"

    for attr in vars(defence):
        # If instance of battlian, need calculations
        if isinstance(getattr(defence, attr, None), Battlian):

            #get min of either all troop of battlian or no of troops required.

            outputList.append(str(min(
                getattr(defence, attr).size - getattr(solution, attr).size,
                getattr(defence, attr).size
                )))
            outputList.append(attr+',')

        else:
            # Name of defence instance
            name = getattr(defence, attr, None) + ' deploys'

    return ("{} {} and {}".format( name.capitalize(),
        (' '.join(outputList)).rstrip(','), gameStatus))
