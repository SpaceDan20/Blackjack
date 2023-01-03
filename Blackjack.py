import random
import os
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
results = {'wins': 0, 'draws': 0, 'losses': 0}

# main game
play = True
while play:
    os.system('cls||clear')
    # draws new set of cards
    player_cards = []
    dealer_cards = []
    player_cards.append(random.choice(cards))
    player_cards.append(random.choice(cards))
    dealer_cards.append(random.choice(cards))
    dealer_cards.append(random.choice(cards))

    # changes ace to 1 if player gets 2 aces at the start
    if sum(player_cards) == 22:
        player_cards.remove(11)
        player_cards.append(1)

    # introducing player to new set of cards
    print("\nWelcome to Blackjack!")
    print(f"Dealer's card: {dealer_cards[0]}")
    print(f"Your cards: {player_cards} = {sum(player_cards)}\n")

    # player draws their cards
    while True:
        draw_or_naw = input("Would you like to draw another card? Type 'y' for yes or 'n' for no: ")
        if draw_or_naw == "y":
            player_cards.append(random.choice(cards))
            # checks for bust and changes ace if in player hand
            if sum(player_cards) > 21:
                if 11 in player_cards:
                    player_cards.remove(11)
                    player_cards.append(1)
                else:
                    break
            print(f"\nDealer's card: {dealer_cards[0]}")
            print(f"Your cards: {player_cards} = {sum(player_cards)}\n")
        elif draw_or_naw == "n":
            break
        else:
            print("\nNot an option. Please type 'y' to draw another card or 'n' to play current cards.\n")

    # changes ace to 1 if dealer gets 2 aces at the start
    if sum(dealer_cards) == 22:
        dealer_cards.remove(11)
        dealer_cards.append(1)

    # dealer draws their cards
    while sum(dealer_cards) < 17:
        dealer_cards.append(random.choice(cards))
        if sum(dealer_cards) > 21 and 11 in dealer_cards:
            dealer_cards.remove(11)
            dealer_cards.append(1)

    # game results
    if sum(player_cards) > 21:
        print("\nPLAYER BUST. You lose.")
        print(f"Dealer's cards: {dealer_cards} = {sum(dealer_cards)}")
        print(f"Your cards: {player_cards} = !!! {sum(player_cards)} !!!\n")
        results["losses"] += 1
    elif sum(dealer_cards) > 21:
        print("\nDEALER BUST. You win!")
        print(f"Dealer's cards: {dealer_cards} = !!! {sum(dealer_cards)} !!!")
        print(f"Your cards: {player_cards} = {sum(player_cards)}\n")
        results["wins"] += 1
    elif sum(player_cards) == sum(dealer_cards):
        print("\nDRAW. Nobody wins.")
        print(f"Dealer's cards: {dealer_cards} = {sum(dealer_cards)}")
        print(f"Your cards: {player_cards} = {sum(player_cards)}\n")
        results["draws"] += 1
    elif sum(player_cards) < sum(dealer_cards):
        if sum(dealer_cards) == 21 and len(dealer_cards) == 2:
            print("\nDealer Blackjack! Dealer wins!")
            print(f"Dealer's cards: {dealer_cards} = *** {sum(dealer_cards)} ***")
        else:
            print("\nDEALER WINS.")
            print(f"Dealer's cards: {dealer_cards} = {sum(dealer_cards)}")
        print(f"Your cards: {player_cards} = {sum(player_cards)}\n")
        results["losses"] += 1
    else:
        if sum(player_cards) == 21 and len(player_cards) == 2:
            print("\nPlayer Blackjack! You win!")
            print(f"Dealer's cards: {dealer_cards} = {sum(dealer_cards)}")
            print(f"Your cards: {player_cards} = *** {sum(player_cards)} ***\n")
        else:
            print("\nPLAYER WINS.")
            print(f"Dealer's cards: {dealer_cards} = {sum(dealer_cards)}")
            print(f"Your cards: {player_cards} = {sum(player_cards)}\n")
        results["wins"] += 1
    # exits game if player decides to quit
    play_again = input("would you like to play again? y or n: ")
    if play_again == "n":
        play = False

# game outro, lists session wins/draws/losses
print("\nThanks for playing Blackjack!")
print(f"Wins: {results['wins']} | Draws: {results['draws']} | Losses: {results['losses']}\n")