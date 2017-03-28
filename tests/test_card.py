#!/usr/bin/env python
# -*- coding: utf-8 -*-

from unittest import TestCase
from blackjack.models import Card
import blackjack.config as cfg


class TestCard(TestCase):

    # Tests for methods
    def test_show_card_method(self):

        # Creates a card.
        self.card = Card(cfg.values[0], cfg.suits[0])

        # Asserts that the card is correctly returned in both long and short forms.
        self.assertEqual(self.card.show_card(True), "Ace of Spades")
        self.assertEqual(self.card.show_card(False), "{}{}".format("A", "\u2660"))
