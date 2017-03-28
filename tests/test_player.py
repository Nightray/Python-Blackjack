#!/usr/bin/env python
# -*- coding: utf-8 -*-

from unittest import TestCase
from blackjack.models import Player, Deck


class TestPlayer(TestCase):

    def setUp(self):

        # Instantiates a player.
        self.player = Player("Player One", Deck())

    def test_if_constructor_creates_a_player(self):

        # Asserts that the player has been correctly created.
        self.assertEquals("Player One", self.player.name)
        self.assertEquals(0, len(self.player.hand))
        self.assertEquals(0, self.player.money)

    def test_draw_card_method(self):

        # Instantiates a new deck of cards and three test players.
        deck = Deck()
        p1 = Player("Player One", deck)
        p2 = Player("Player Two", deck)
        p3 = Player("Player Three", deck)

        # Draws cards for all the players using three different methods.
        p1.draw_card().draw_card().draw_card()
        p2.draw_card()
        p2.draw_card()
        p3.draw_cards(2)  # Alias. Because I can. (<-- notice the period. Because I can.)

        # Asserts that all methods of drawing cards are working
        self.assertEquals(3, len(p1.hand))
        self.assertEquals(2, len(p2.hand))
        self.assertEquals(52-3-2-2, len(deck.cards))

    def test_discard_hand_method(self):

        # Draws two cards into the player's hand and discards the hand.
        self.player.draw_cards(2)
        self.player.discard_hand()

        # Asserts that the hand has been correctly discarded to the discard pile.
        self.assertEquals(2, len(self.player.deck.discards))
