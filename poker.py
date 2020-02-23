from carddeck import Carddeck
import output

number_of_players = int(input("How many Players? "))
pos_flop = number_of_players * 2 + 1
pos_turn = number_of_players * 2 + 5
pos_river = number_of_players * 2 + 7
print(pos_flop, pos_turn, pos_river)
pokerdeck = Carddeck()

Carddeck.mix(pokerdeck.deck)

def give_hand(pokerdeck):
    print("\nHand:")
    for player in range(number_of_players):
        print("Player%2d:" %player)
        for i in range(player * 2, player * 2 + 2):
            output.out_single_card(pokerdeck.deck[i])

def give_flop(pokerdeck):
    print("\nFlop:")
    for player in range(pos_flop, pos_flop + 2):
        output.out_single_card(pokerdeck.deck[player])

def give_turn(pokerdeck):
    print("\nTurn:")
    output.out_single_card(pokerdeck.deck[pos_turn])

def give_river(pokerdeck):
    print("\nRiver:")
    output.out_single_card(pokerdeck.deck[pos_river])


give_hand(pokerdeck)
give_flop(pokerdeck)
give_turn(pokerdeck)
give_river(pokerdeck)
