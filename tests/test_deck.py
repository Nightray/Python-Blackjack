#!/usr/bin/env python
# -*- coding: utf-8 -*-

from unittest import TestCase
from blackjack.models import Deck


class TestDeck(TestCase):

    # Tests for the constructor
    def test_if_constructor_creates_an_unshuffled_deck_of_cards(self):

        # Instantiates an unshuffled deck.
        deck = Deck(False)

        # Checks if the deck has a correct length.
        self.assertEquals(len(deck.cards), 52)
        self.assertEquals(len(deck.discards), 0)

        # Checks if the cards are in a correct order.
        self.assertEquals(deck.cards[0].show_card(True), "Ace of Spades")
        self.assertEquals(deck.cards[22].show_card(True), "Ten of Diamonds")
        self.assertEquals(deck.cards[35].show_card(True), "Ten of Clubs")
        self.assertEquals(deck.cards[51].show_card(True), "King of Hearts")

    def test_if_constructor_creates_a_shuffled_deck_of_cards(self):

        # Instantiates an unshuffled deck and lists all cards in a variable.
        ordered_deck = Deck(False)
        ordered_deck = list(map(lambda x: x.show_card(), ordered_deck.cards))

        # Instantiates a shuffled deck and lists all cards in a variable.
        unordered_deck = Deck(True)
        unordered_deck = list(map(lambda x: x.show_card(), unordered_deck.cards))

        # Asserts that cards in both lists are in different orders.
        self.assertNotEquals(unordered_deck, ordered_deck)

    # Tests for methods
    def test_shuffle_method_no_discards(self):

        # Instantiates an unshuffled deck and saves all cards in a list.
        deck = Deck(False)
        ordered_deck = list(map(lambda x: x.show_card(), deck.cards))

        # Shuffles the deck and saves all cards in a list.
        deck.shuffle(False)
        unordered_deck = list(map(lambda x: x.show_card(), deck.cards))

        # Asserts that the deck was successfully shuffled, and that it's length didn't change.
        self.assertCountEqual(unordered_deck, ordered_deck)
        self.assertNotEquals(unordered_deck, ordered_deck)

    def test_shuffle_method_with_discards(self):

        # Instantiates an unshuffled deck and saves all cards in a list.
        deck = Deck(False)
        ordered_deck = list(map(lambda x: x.show_card(), deck.cards))

        # Moves cards from the deck to a discard pile, then shuffles the deck and saves all cards in a list.
        deck.discard_card(deck.deal_card())
        deck.discard_card(deck.deal_card())
        deck.discard_card(deck.deal_card())
        deck.shuffle(True)
        unordered_deck = list(map(lambda x: x.show_card(), deck.cards))

        # Asserts that the deck was successfully shuffled along with the cards from the discard pile.
        self.assertCountEqual(unordered_deck, ordered_deck)
        self.assertNotEquals(unordered_deck, ordered_deck)
        self.assertEquals(len(deck.discards), 0)

    def test_deal_card_method(self):

        # Instantiates an unshuffled deck, saves it length to a variable, then transfers a card to another list.
        deck = Deck(False)
        deck_len_before = len(deck.cards)
        removed_card = [deck.deal_card()]

        # Asserts that the card has been correctly removed from one list, and transferred to another.
        self.assertEquals(len(deck.cards), deck_len_before - 1)
        self.assertEquals(len(removed_card), 1)

    def test_add_to_discard_pile_method(self):

        # Instantiates an unshuffled deck and saves it length, then moves two cards to the discard pile.
        deck = Deck(False)
        deck_len_before = len(deck.cards)
        deck.discard_card(deck.deal_card())
        deck.discard_card(deck.deal_card())

        # Asserts that cards have been correctly moved to the discard pile.
        self.assertEquals(len(deck.discards), 2)
        self.assertEquals(len(deck.cards), deck_len_before - 2)
