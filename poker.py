from carddeck import Carddeck
import output

test_deck = Carddeck()

Carddeck.mix(test_deck.deck)
output.out_single_card(test_deck.deck[0])