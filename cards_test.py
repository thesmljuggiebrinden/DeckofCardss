from behave import *

import deckofcards


@Given('I have created a new deck object')
def step_impl(context):
    pass


@When('I create the new class')
def step_impl(context):
    new_deck = deckofcards.Deck
    assert new_deck is not None
    context.card_holder = new_deck
    assert context.new_deck.deck_of_cards.__len__() == 52


@Then('the number of cards should be recorded')
def step_impl(context):
    assert context.card_holder.count == context.num_of_cards


@Given('I have a set of cards')
def step_impl(context):
    context.card_deck = deckofcards.Deck
    assert context.card_deck is not None


@When('I draw a card')
def step_impl(context):
    context.num_of_cards = context.new_deck.deck_of_cards.__len__()
    context.drawn_card = context.new_deck.get_card()
    assert context.drawn_card is not None


@Then('It is removed from the deck')
def step_impl(context):
    assert context.new_deck.deck_of_cards.__len__() < context.num_of_cards
    assert context.drawn_card not in context.new_deck.deck_of_cards


@Given('I have a deck of cards')
def step_impl(context):
    context.new_deck = deckofcards.Deck


@When('I shuffle them')
def step_impl(context):
    context.before_shuffle = context.new_deck
    context.after_shuffle = context.new_deck.shuffle_deck()


@Then('The order has changed')
def step_impl(context):
    assert context.before_shuffle != context.after_shuffle


@Given('I have a new deck of cards')
def step_impl(context):
    context.new_deck = deckofcards.Deck


@When('I create a hand')
def step_impl(context):
    context.new_hand = deckofcards.Hand(context.new_hand, 5)
    assert context.new_hand is not None


@Then('my hand has 5 cards')
def step_impl(context):
    assert context.new_hand.hand_of_cards.__len__() == 5