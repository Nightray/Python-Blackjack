#!/usr/bin/env python
# -*- coding: utf-8 -*-

from random import randint
import blackjack.config as cfg


class Card:

    def __init__(self, value, suit):

        # Variables
        self._value = value["name"]
        self._short_value = value["short_name"]

        self._suit = suit["name"]
        self._symbol = suit["symbol_black"]

    def show_card(self, show_full=False):
        if show_full:
            return "{} of {}".format(self._value, self._suit)
        else:
            return "{}{}".format(self._short_value, self._symbol)


class Deck:

    def __init__(self, shuffle=True):

        # Variables
        self._suits = cfg.suits
        self._values = cfg.values
        self.cards = []
        self.discards = []

        self._create()

        if shuffle:
            self.shuffle(False)

    def _create(self):
        self.cards = []
        for i in range(len(self._suits) * len(self._values)):
            self.cards.append(Card(self._values[i % len(self._values)],
                                   self._suits[i // len(self._values)]))

    def shuffle(self, shuffle_discards=True):

        if shuffle_discards:
            self.cards += self.discards
            self.discards = []

        for i in range(len(self.cards) - 1, 0, -1):
            random_int = randint(0, i)
            self.cards[i], self.cards[random_int] = self.cards[random_int], self.cards[i]

    def deal_card(self):
        return self.cards.pop()

    def discard_card(self, card):
        self.discards.append(card)

    # Aliases
    def arrange_in_order(self):
        self._create()


class Player:

    def __init__(self, _name, _deck):
        self.name = _name
        self.deck = _deck
        self.money = 0
        self.hand = []

    def draw_card(self, _number_of_cards=1):
        [self.hand.append(self.deck.deal_card()) for _ in range(_number_of_cards)]
        return self

    def discard_hand(self):
        for card in self.hand:
            self.deck.discard_card(card)

    # Aliases
    def draw_cards(self, _number_of_cards):
        # Yes, this is just an alias. You can totally draw multiple cards with draw_card() method. The cake is a lie ~!
        self.draw_card(_number_of_cards)
