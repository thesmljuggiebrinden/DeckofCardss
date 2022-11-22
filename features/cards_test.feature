Feature: testing all card classes
  Scenario: test that card values are recorded correctly
    Given I have created a new deck object
    When I create the new class
    Then the card value should be recorded

  Scenario: drawing a card removes it from the list
    Given I have a set number of cards
    When I draw a card
    Then it is removed from the deck

  Scenario: shuffling the deck changes the order
    Given I have a deck of cards
    When I shuffle them
    Then the order has changed

  Scenario: building a hand records correctly
    Given I have a new deck of cards
    When I create a hand
    Then my hand has 5 cards