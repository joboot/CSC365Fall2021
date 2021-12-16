"""
This is a game called Game 21 that is based off of blackjack
"""

__author__ = "Jordan Booth"
__version__ = "1.0"
__date__ = "11.30.2021"
__status__ = "Development"

import utils
import random


def main():
    """
    Inputs:
    Player name
    Whether or not they want to draw another card
    Whether or not they want to double down
    Whether or not they want to continue playing

    Outputs:
    Title
    Rules
    Dealing to players and dealer
    End of round summary with winners and cash left
    :return:
    """
    num_players_out = 0
    players = {}
    display_intro()
    get_players(players)

    while True:

        play_round(players)

        for player_name, player_info in players.items():

            cash, cards, cards_total, bet = player_info.values()

            if cash < .25:
                num_players_out += 1
                continue

        if num_players_out == len(players):
            utils.display_line()
            print("Game over!  All players are out of the game")
            utils.display_line()
            break

        user_input = utils.get_yn("Would you like to play another round? (y/n)? ")

        if not user_input:
            utils.display_line()
            print("Thanks for playing! Come back soon!")
            utils.display_line()
            break


def display_intro():
    """
    Displays the game title and rules
    :return: n/a
    """
    utils.display_line()
    print("\t\t   _________    __  _________   ___  ___\n" +
          "\t\t  / ____/   |  /  |/  / ____/  |__ \<  /\n" +
          "\t\t / / __/ /| | / /|_/ / __/     __/ // / \n" +
          "\t\t/ /_/ / ___ |/ /  / / /___    / __// /  \n" +
          "\t\t\____/_/  |_/_/  /_/_____/   /____/_/   \n")
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
          "9. Winner is the last person with cash, not including the dealer.")
    utils.display_line()


def get_players(players):
    """
    Get the player's names and then add the player to the dictionary setting up initial player's data
    Until the user enters the word 'done' symbolizing no more players
        set cash to $1.0
        set cards to an empty list
        set cards_total to 0
        set bet to 0.25 default value
    :return: n/a
    """
    print("Now lets get this game setup.  Who is all playing?\n" +
          "Please enter a player's name or enter 'done' when finished.\n")

    while True:
        player_name = input("Please enter the players name: ")

        if player_name.lower() == "done":
            break

        players[player_name] = {
            "cash": 1.0,
            "cards": [],
            "cards_total": 0,
            "bet": .25
        }


def play_round(players):
    """
    Call each function required to play one round
        1) setup the new round
        2) deal to each player
        3) deal to the dealer
        4) display the winners
    :param players: 2D Dictionary of all player's data
    :return: n/a
    """
    utils.display_line()
    print("Starting Game...")
    utils.display_line()
    print()

    setup_new_round(players)
    deal_to_players(players)
    dealer_cards_total = deal_to_dealer(players)
    display_winners(players, dealer_cards_total)


def setup_new_round(players):
    """
    Reset all player's data for the next round.
        set cards to an empty list
        set cards_total to 0
        set bet to 0.25
    :param players: 2D dictionary of the player's data
    :return:  n/a
    """
    for player_name, player_info in players.items():
        player_info['cards'] = []
        player_info['cards_total'] = 0
        player_info['bet'] = .25


def deal_card(player_info):
    """
    Do the following three items:
        Generate a random number between 1-10
        add it to the card to the list of cards
        add the card value to the cards total
    :param player_info: one player's sub dictionary of cards, and cards_total
    :return: n/a
    """
    card_num = random.randint(1, 10)
    player_info['cards'].append(card_num)
    player_info['cards_total'] += card_num


def deal_to_players(players):
    """
    Deal to all players using a for loop through the 2D dictionary
        if the player is out of money then continue
        else automatically deal them two cards
        and then ask the player if they want another cards as long as they don't exceed 21
        if they exceed 21 then continue to the next player
        else ask them if they want to double their bet as long as they have at least 50 cents
    :param players: 2D dictionary storing all player's data
    :return: n/a
    """
    for player_name, player_info in players.items():
        cash, cards, cards_total, bet = player_info.values()

        if cash < .25:
            continue

        print("Dealing to " + player_name)

        deal_card(player_info)
        deal_card(player_info)

        while True:
            cash, cards, cards_total, bet = player_info.values()
            display_cards(cards)

            if cards_total > 21:
                print(player_name + "'s hand exceeded 21")
                break

            print()
            user_input = utils.get_yn("Would you like another card (y/n)? ")

            if user_input:
                deal_card(player_info)

            else:
                cash, cards, cards_total, bet = player_info.values()
                print(player_name, "holds at", cards_total)

                user_input = utils.get_yn("Do you want to double down (y/n)? ")

                if user_input:
                    player_info['bet'] += .25

                break


def deal_to_dealer(players):
    """
    if there are no players still playing this hand (they did not exceed 21)
    then the dealer automatically wins
    otherwise start dealing to the dealer until he beats all players or reaches 21
    :param players: 2D dictionary storing all player's data
    :return: n/a
    """
    num_players_out = 0
    highest_hand = 0

    for player, player_info in players.items():
        cards_total = player_info['cards_total']
        if cards_total > 21:
            num_players_out += 1
        elif cards_total > highest_hand:
            highest_hand = cards_total

    if num_players_out == len(players):
        print("Dealer wins!")
        return 21  # dealer auto win

    print("Dealing to dealer")

    dealer_cards = []
    dealer_cards_total = 0

    while True:
        card_num = random.randint(1, 10)
        dealer_cards.append(card_num)
        dealer_cards_total += card_num

        if dealer_cards_total > 21:
            display_cards(dealer_cards)
            print("Dealer's hand exceeded 21")
            return dealer_cards_total

        elif dealer_cards_total > highest_hand:
            display_cards(dealer_cards)
            print("Dealer holds at", dealer_cards_total)
            print("Dealer wins!")
            return dealer_cards_total


def display_cards(cards):
    """
    Display one player's current list of cards on one line
    :param cards: one player's current cards
    :return: n/a
    """
    print('  Cards: ', end='')
    for card in cards:
        print(str(card) + ' ', end='')
    print()


def display_winners(players, dealer_cards_total):
    """
    Display the winners for the current round
    :param players: 2D dictionary of all player's data
    :param dealer_cards_total: the dealer's card total
    :return: n/a
    """
    total_winners = 0
    num_players_out = 0

    print()

    for player_name, player_info in players.items():

        cash, cards, cards_total, bet = player_info.values()

        if cash < 0.25:
            num_players_out += 1
            continue

        if dealer_cards_total > 21:

            if cards_total <= 21:
                total_winners += 1
                player_info['cash'] += bet
                print(player_name, "is a winner!")

                print()

            else:
                player_info['cash'] -= bet

        else:
            player_info['cash'] -= bet

    display_round_summary(players)


def display_round_summary(players):
    """
    Display the round summary, how much money check player current has
    :param players: 2D dictionary of all player's data
    :return: the number of players who still has cash
    """
    for player_name, player_info in players.items():
        cash, cards, cards_total, bet = player_info.values()

        print(
            f'{player_name + "s balance:":<30s}'
            f'{"$"}'
            f'{str(cash):>6s}')

    print()


# runs this specific module's main
if __name__ == "__main__":
    main()
