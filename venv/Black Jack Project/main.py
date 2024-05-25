from game import Game
from deck import Deck
from hand import Hand
from money import Money
import sys

print("Welcome to BlackJack")
money = Money(5000)

while True:
    # Check if player has run out of money
    if money.amount <=0:
        print("It is good that you weren't playing with real money")
        print("Thanks for playing")
        sys.exit()
    #Ask player to enter their bet
    print("Money: ", money.amount)
    #Get bet
    bet = money.get_bet(money.amount)
    # Get deck
    deck = Deck()
    deck.shuffle()
    #Give the dealer and player two cards from the deck
    player_hand = Hand()
    dealer_hand = Hand(dealer=True)

    for i in range(2):
        player_hand.add_card(deck.deal())
        dealer_hand.add_card(deck.deal())

    # Hanlde player actions
    print("Bet: ",bet)

    while True:
        dealer_hand.display()
        player_hand.display()
        print()
        # Check if player has bust
        if player_hand.get_value() >21:
            break
        # Get Player's move
        game = Game()
        move = game.get_move(player_hand.get_value(),money.amount- bet)
        #Handle player move
        if move == 'D':
            additional_bet= money.get_bet(min(bet,(money-bet)))
            bet += additional_bet
            print(f"Bet increased to {bet}.")
            print("Bet: ",bet)
        if move in ('H','D'):
            #Get another card
            new_card = deck.deal()
            rank = new_card.get_rank()
            suit = new_card.get_suit()
            print(f"You drew a {rank} of {suit}.")
            player_hand.add_card(new_card)
            if player_hand.get_value()>21:
                continue
        if move == 'S':
            break

    # Handle dealer's action
    if player_hand.get_value()<=21:
        while dealer_hand.get_value()<17:
            #The dealers hit
            print("The dealer hit...")
            dealer_hand.add_card(deck.deal())
            dealer_hand.display()
            player_hand.display()
            if dealer_hand.get_value() >21:
                break
            input("Pres enter to continue.")
            print('\n\n')
    #Handle whether the player won or lost or draw
    dealer_hand.display(show_dealer=True)
    player_hand.display()
    player_value = player_hand.get_value()
    dealer_value = dealer_hand.get_value()

    if dealer_value >21:
        print(f"Dealer busts! You win ${bet}.")
        money.add_money(bet)
    elif player_value >21 or player_value < dealer_value:
        print(f"You lost!")
        money.sub_money(bet)
    elif player_value > dealer_value:
        print(f"You win ${bet}")
        money.add_money(bet)
    elif player_value == dealer_value:
        print(f"It is a draw and the bet is return to you")
        input("Pres enter to continue")
        print('\n\n')


    

