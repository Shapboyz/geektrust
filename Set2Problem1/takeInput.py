from Set2Problem1.war import createRegion, compareArmyStrength

def user_input():
    """ Function to take user input and create instance for falicornia army.
        Returns a instance of Falicornia army if user input is required
        format else it return False.
    """
    try:
        userinput = input("Input: ")

        userinput = userinput.replace(',', '').split('with ')
        name = userinput[0].split(' ')[0]
        userinput = userinput[-1].rstrip(' ').split(' ')
        return createRegion(name= name,userInput = userinput)

    except:
        return False

def take_input(counter):
    """ Function for handling user input, creating a instance from user input.
        creating a instance of lengburuself.
        In case if the user input is not in proper format, it retries for
        three times. that can be configurable from Main function as value of
        counter.

        Args:
            Param1(int) : counter - to set number of retries for user input.

        External Methods :
            createRegion : To create instance of class Region.
            compareArmyStrength : To check deployment of lengburu army.

    """

    falicornia = user_input()
    lengburu = createRegion(name="lengburu")
    if falicornia:
        print(compareArmyStrength(lengburu, falicornia))

        # Need to create army for another_planet and run as below
        # compareArmyStrength(lengburu, another_planet)

        exit(0)  # exit the program once done.
    else:
        while (counter if isinstance(counter, int) else False):
            counter -=1
            counter = take_input(counter)
        exit(1) # exit the program if failed for 3 times.
