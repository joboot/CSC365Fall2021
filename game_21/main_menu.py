"""

"""

__author__ = "Jordan Booth"
__version__ = "1.0"
__date__ = "11.30.2021"
__status__ = "Development"

import utils


def main():
    """

    :return:
    """
    display_rules()
    display_menu()


def display_rules():
    """

    :return:
    """
    utils.display_line()
    print("\t\t   _________    __  _________   ___  ___")
    print("\t\t  / ____/   |  /  |/  / ____/  |__ \<  /")
    print("\t\t / / __/ /| | / /|_/ / __/     __/ // / ")
    print("\t\t/ /_/ / ___ |/ /  / / /___    / __// /  ")
    print("\t\t\____/_/  |_/_/  /_/_____/   /____/_/   ")
    utils.display_line()

    print("The rules are simple!\n" +
          "1. Each player is trying to get as close to 21 without going over.\n" +
          "2. Each player is ONLY trying to beat the dealer's hand.\n" +
          "3. The dealer will keep dealing himself cards\n" +
          "until he beats all players hands or goes over 21.\n" +
          "4. Tie goes to the player, not the dealer.\n" +
          "5. Each player gets dealt two card between 1 - 10.\n" +
          "6. The player then can choose to receive additional cards.\n" +
          "7. Each player starts with $1.00.\n" +
          "8. Default bet is 25 cents, but the player can double it after holding.\n" +
          "9. Winner is the last person with cash, not including the dealer.\n")
    utils.display_line()


def display_menu():
    """

    :return:
    """
    print("Now lets get this game setup.  Who is all playing?\n" +
          "Please enter a player's name or enter 'done' when finished.")


# runs this specific module's main
if __name__ == "__main__":
    main()
