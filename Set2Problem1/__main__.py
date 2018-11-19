from takeInput import take_input
import sys


def main():
    """ Main function to start program, runs the input function with
        counter set to 3.
    """

    if sys.version_info[0] > 2 and sys.version_info[1] > 5:
        take_input(2)
    else:
        raise Exception("Python 3.6 or a more recent version is required.")



if __name__ == "__main__":
    main()
